import subprocess
import shutil

class LLMClient:
    def __init__(self, model="mistral"):
        if not shutil.which("ollama"):
            raise RuntimeError("Ollama is not installed or not in PATH")
        self.model = model

    def generate(self, prompt: str) -> str:
        try:
            result = subprocess.run(
                [
                    "ollama",
                    "run",
                    self.model,
                    prompt
                ],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                timeout=180
            )
        except subprocess.TimeoutExpired:
            raise RuntimeError("Ollama request timed out")

        if result.returncode != 0:
            raise RuntimeError(result.stderr.decode("utf-8"))

        return result.stdout.decode("utf-8").strip()
