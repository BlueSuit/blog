FROM public.ecr.aws/lambda/python:3.8

RUN /var/lang/bin/python3.8 -m pip install --upgrade pip

WORKDIR ${LAMBDA_TASK_ROOT}

COPY temp_files ${LAMBDA_TASK_ROOT}
RUN pip install -r combined_requirements.txt
COPY src ${LAMBDA_TASK_ROOT}


CMD ["app.lambda_handler"]