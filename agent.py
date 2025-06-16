import os
import subprocess
import docker
import yaml
from pathlib import Path
from typing import Dict, Any

class CodeGeneratorAgent:
    def __init__(self):
        self.docker_client = docker.from_env()
        self.project_config = self._load_config()
        
    def _load_config(self) -> Dict[str, Any]:
        """Load configuration from YAML file"""
        config_path = Path('config/agent_config.yaml')
        if config_path.exists():
            with open(config_path, 'r') as f:
                return yaml.safe_load(f)
        return {}

    def generate_code(self, requirements: str) -> str:
        """Generate code based on requirements"""
        # This would integrate with an LLM in production
        # For now, we'll use a simple template
        return f"""# Generated code based on: {requirements}
def main():
    print("Hello from generated code!")

if __name__ == "__main__":
    main()
"""

    def build_docker_image(self, dockerfile_path: str, tag: str) -> bool:
        """Build a Docker image from the specified Dockerfile"""
        try:
            self.docker_client.images.build(
                path=os.path.dirname(dockerfile_path),
                tag=tag,
                dockerfile=os.path.basename(dockerfile_path)
            )
            return True
        except Exception as e:
            print(f"Error building Docker image: {e}")
            return False

    def run_docker_container(self, image_name: str, command: str = None) -> bool:
        """Run a Docker container from the specified image"""
        try:
            self.docker_client.containers.run(
                image_name,
                command=command,
                detach=True,
                auto_remove=True
            )
            return True
        except Exception as e:
            print(f"Error running Docker container: {e}")
            return False

if __name__ == "__main__":
    agent = CodeGeneratorAgent()
    
    # Example usage
    generated_code = agent.generate_code("Simple Python script")
    with open("generated_code.py", "w") as f:
        f.write(generated_code)
    
    # Build and run Docker container
    if agent.build_docker_image("Dockerfile", "my-agent"):
        print("Docker image built successfully")
        if agent.run_docker_container("my-agent", "python generated_code.py"):
            print("Docker container running successfully")