# FAQ

## Can I Run This Without A GPU?

Yes. Dataset tools, dry runs, reports, tests, docs, notebooks, and the dashboard work without a GPU.

## When Do I Need A GPU?

You need a CUDA GPU for real LoRA or QLoRA training and likely for real adapter export workflows.

## Does Dry Run Train A Model?

No. Dry run validates configs and writes planning artifacts. It does not load a model or train weights.

## Does GGUF Export Create A Real Model File?

Dry run export creates a manifest only. Real export needs Unsloth, model access, a trained adapter, and enough disk space.

## Does Ollama Need To Be Installed?

Not for dry run planning or tests. Real Ollama commands need Ollama installed and available on `PATH`.

## Are The Finance Examples Real?

No. They are synthetic examples for learning. Do not treat output as financial advice.

## Where Are Generated Files Written?

Generated files go under:

- `experiments\`
- `exports\`

Those generated outputs are ignored except for folder README files.
