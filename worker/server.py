from typing import List
from fastapi import FastAPI
from pydantic import BaseModel, Field


app = FastAPI()


class JobConfig(BaseModel):
    type: str = Field(const=True)


class InterpolationAnimationJobConfig(BaseModel):
    type: str = Field(const=True, default="interpolation_animation")


class Job(BaseModel):
    config: JobConfig


_jobs = []
_prefix = "/api/v1"

app.post(_prefix + "/job")
def add_job(job: Job) -> str:
    _jobs.append(job)
    return "job added"

app.get(_prefix + "/job", response_model=List[Job])
def get_jobs() -> List[Job]:
    return _jobs


if __name__ == "__main__":
    from uvicorn import run
    run(app, host="0.0.0.0")
