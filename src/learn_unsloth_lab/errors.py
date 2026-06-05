class LabError(Exception): pass
class ConfigError(LabError): pass
class DatasetError(LabError): pass
class ModelError(LabError): pass
class TrainingError(LabError): pass
class EvaluationError(LabError): pass
class ExportError(LabError): pass
