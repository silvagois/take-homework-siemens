#!/usr/bin/env python3
import os
from aws_cdk import core
from log_analysis_stack import LogAnalysisStack

app = core.App()
LogAnalysisStack(app, "LogAnalysisStack")

app.synth()