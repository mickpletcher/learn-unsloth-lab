DEFAULT_TEMPLATE="""{{ if .System }}<|system|>\n{{ .System }}{{ end }}\n<|user|>\n{{ .Prompt }}\n<|assistant|>\n"""
