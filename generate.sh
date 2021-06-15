#!/bin/bash
echo "Generating proto grpc files..."
python -m grpc_tools.protoc -I=src/resources --python_out=src/resources --grpc_python_out=src/resources src/resources/chat.proto
echo "DONE"
