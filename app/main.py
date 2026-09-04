"""FastAPI application that exposes calculator operations."""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, ConfigDict

from app.calculator import add, divide, multiply, subtract


app = FastAPI(
    title="API Calculadora",
    description="API REST simple para sumar, restar, multiplicar y dividir.",
    version="1.0.0",
)


class OperationRequest(BaseModel):
    """Input model for a calculator operation."""

    model_config = ConfigDict(extra="forbid")

    a: float
    b: float


class OperationResponse(BaseModel):
    """Output model for a calculator operation."""

    operation: str
    a: float
    b: float
    result: float


@app.get("/")
def root() -> dict[str, str]:
    """Return a simple health message."""
    return {"message": "API Calculadora funcionando"}


@app.post("/sumar", response_model=OperationResponse)
def sum_numbers(request: OperationRequest) -> OperationResponse:
    """Add two numbers."""
    return OperationResponse(
        operation="sumar",
        a=request.a,
        b=request.b,
        result=add(request.a, request.b),
    )


@app.post("/restar", response_model=OperationResponse)
def subtract_numbers(request: OperationRequest) -> OperationResponse:
    """Subtract the second number from the first."""
    return OperationResponse(
        operation="restar",
        a=request.a,
        b=request.b,
        result=subtract(request.a, request.b),
    )


@app.post("/multiplicar", response_model=OperationResponse)
def multiply_numbers(request: OperationRequest) -> OperationResponse:
    """Multiply two numbers."""
    return OperationResponse(
        operation="multiplicar",
        a=request.a,
        b=request.b,
        result=multiply(request.a, request.b),
    )


@app.post("/dividir", response_model=OperationResponse)
def divide_numbers(request: OperationRequest) -> OperationResponse:
    """Divide the first number by the second."""
    try:
        result = divide(request.a, request.b)
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc

    return OperationResponse(
        operation="dividir",
        a=request.a,
        b=request.b,
        result=result,
    )
