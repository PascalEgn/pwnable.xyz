#!/bin/bash
docker run --cap-add=SYS_PTRACE --security-opt seccomp=unconfined -it -v /Users/pascalegner/pwnable.xyz:/pwnable:z -w /pwnable ree_image_v2:latest /bin/bash



# docker run -it ree_image:latest /bin/bash
