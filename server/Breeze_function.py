from transformers import AutoTokenizer
from ctransformers import AutoModelForCausalLM
    
def Breeze(question):
    
    # Set gpu_layers to the number of layers to offload to GPU. Set to 0 if no GPU acceleration is available on your system.
    llm = AutoModelForCausalLM.from_pretrained(
        "YC-Chen/Breeze-7B-Instruct-v1_0-GGUF",
        model_file="breeze-7b-instruct-v1_0-q6_k.gguf",
        model_type="mistral",
        context_length=8000,
        gpu_layers=0,
    )
    
    tokenizer = AutoTokenizer.from_pretrained("MediaTek-Research/Breeze-7B-Instruct-v1_0")
    
    gen_kwargs = dict(
        max_new_tokens=1024,
        repetition_penalty=1.1,
        stop=["[INST]"],
        temperature=0.0,
        top_p=0.0,
        top_k=1,
    )
    answer = ""
    chat = [
      {"role": "system", "content": "Below is an instruction that describes a task. Write a response that appropriately completes the request in Traditional Chinese."},
      {"role": "user", "content": question}
    ]
    
    for text in llm(tokenizer.apply_chat_template(chat, tokenize=False), stream=True, **gen_kwargs):
        answer = answer + text
    
    print("question : ", question)
    
    if (len(answer) < 3):
        return "抱歉，我不理解你的問題"
    
    print("answer", answer)
    print("-----------------------------")
    return answer
