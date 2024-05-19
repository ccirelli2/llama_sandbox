# llama_sandbox
Sandbox for deploying and testing a local deployment of llama3

# References
- meta llama page
  - https://llama.meta.com/
- model-src-code
  - https://llama.meta.com/llama3/
- articles
  - https://medium.com/@ignacio.de.gregorio.noblejas/meta-releases-llama-3-heres-all-you-need-to-know-88d850cabedd
- model-notes
  - llama3
    - context window: 8k
- model
  - https://huggingface.co/meta-llama
- Local Deployment
    - ollama: https://ollama.com/
- Quantization
    - https://github.com/TimDettmers/bitsandbytes
- Embeddings
  - llama: https://api.python.langchain.com/en/latest/embeddings/langchain_community.embeddings.llamacpp.LlamaCppEmbeddings.html
  - src: https://github.com/ollama/ollama
- Fine Tuning
  - https://github.com/meta-llama/llama-recipes/tree/main
  - Includes tokenizer and prompt template.
- Tokenizer
  - https://llama.meta.com/docs/model-cards-and-prompt-formats/meta-llama-3/#special-tokens-used-with-meta-llama-3
- Llama Recipes Python Package
  - pip install llama-recipes
- Research Paper - Saftey Tuned Llamas
  - https://arxiv.org/html/2309.07875v3
  - Training large language models to follow instructions makes them perform better on a wide range of tasks and generally become more helpful. However, a perfectly helpful model will follow even the most malicious instructions and readily generate harmful content. In this paper, we raise concerns over the safety of models that only emphasize helpfulness, not harmlessness, in their instruction-tuning. We show that several popular instruction-tuned models are highly unsafe
- Model Evaluation Library
  - https://github.com/EleutherAI/lm-evaluation-harness
- Google Evaluator Safe Model
  - https://ai.google.dev/responsible