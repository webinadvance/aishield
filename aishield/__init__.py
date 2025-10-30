"""AIShield - Intelligent Code Obfuscator Against AI Detection"""

__version__ = "1.1.3"
__author__ = "AIShield Contributors"

from .minify import ObfuscationEngine, LanguageRegistry

# Aliases for backward compatibility
CodeObfuscator = ObfuscationEngine
CodeUnobfuscator = None  # Placeholder

__all__ = ["ObfuscationEngine", "LanguageRegistry", "CodeObfuscator", "__version__"]
