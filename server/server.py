from Breeze_function import Breeze
from Embedding import chromaDB_initialize, embedding_generate, retrieve_advices
from prompt import GENERATE_ADVICES_PROMPT, COMPARE_RELEVANCE_MESSAGE_PROMPT
from fastapi import APIRouter
from fastapi.responses import JSONResponse

# Create a new API router
router = APIRouter()

# Endpoint to check the server status
@router.get("/check_server_status")
def test():
    return JSONResponse(content={"success": "true", "message": "API is up and running"})

# Endpoint to generate text based on input string
@router.get("/generate_text")
def generate_text(input_string: str):
    output_string = Breeze(input_string)  # Call the Breeze function to generate text
    return JSONResponse(content={"result": output_string})

# Endpoint to generate advice based on disease name, factor, and customized content
@router.get("/generate_advices")
def generate_advices(disease_name: str, disease_factor: str, patient_customized_content: str):
    prompt_input = "我的檢查結果有 " + str(disease_name) + " 問題，是因為有 " + str(disease_factor) + " 的因素，主要可能的原因以及改善的方式有 " + patient_customized_content + "可以幫我只依照以上的內容輸出一段100至150字的建議，指引我在生活中要如何改善這個疾病的建議給我嗎"
    output_string = Breeze(prompt_input)
    return JSONResponse(content={"result": output_string})

# Endpoint to generate schedule based on disease name, factor, and customized content
@router.get("/generate_schedule")
def generate_schedule(disease_name: str, disease_factor: str, patient_customized_content: str):
    prompt_input = "我的檢查結果有 " + str(disease_name) + " 問題，是因為有 " + str(disease_factor) + " 的因素，主要可能的原因以及改善的方式有 " + patient_customized_content + "可以幫我只依照以上的內容輸出建議我改善生活狀態的排成，我需要一周的計劃表(周一至周日)，我希望一天以早上、下午、晚上三個時段來區隔，主要以餐點以及運動來給予建議，並且以markdown的語法來幫我製作表格以及建議執行的內容應該要多元化，餐點(早餐、中餐、晚餐)要依照情況進行客製化，同一份規畫不能重複超過三次，來安排我未來一周的行程"
    output_string = Breeze(prompt_input)
    return JSONResponse(content={"result": output_string})

@router.get("/get_retireve_advices")
def get_retireve_advices(query):
    # print(retrieve_advices(query))
    return JSONResponse(content={"advices": retrieve_advices(query)})

@router.get("/user_input_query_preprocess")
def user_input_query_preprocess(query):

    advices = retrieve_advices(query)

    keywords_list = ["心臟病"]
    for words_num in range(0, len(keywords_list)):
        if keywords_list[words_num] in query:
            #去資料庫提取相關資料
            data = 200
            query = query + "病患血壓的數據為 : " + str(data)
    
    query = query + GENERATE_ADVICES_PROMPT + advices

    return JSONResponse(content={"advices": Breeze(query)})
