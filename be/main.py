from fastapi import FastAPI,UploadFile,Form,File
from db import supabase_client_object
app=FastAPI()


@app.post("/profile_recruiter")
async def profile_recruiter_function(
    pic: UploadFile = File(...),
    experience: int = Form(...),
    company: str = Form(...),
    user_id:str=Form(...)
):
    print(experience,company)
    file_data = await pic.read()

    file_name = pic.filename

    supabase_client_object.storage.from_("r_profiles_files").upload(
        file_name,
        file_data
    )

    p_url = supabase_client_object.storage.from_(
        "r_profiles_files"
    ).get_public_url(file_name)

    supabase_client_object.table("recruiter_profiles").insert({
        "pic": p_url,
        "experience": experience,
        "company": company,
        "user_id":user_id
    }).execute()

    return {
        "msg": "Profile Created Successfully",
        "pic_url": p_url
    }

@app.post("/register")
def register_function(payload:dict):
    
    if payload["password"] == payload["confirm_password"]:
        supabase_client_object.table("users").insert({
            "name":payload["name"],
            "email":payload["email"],
            "password":payload["password"],
            "role":payload["role"]
        }).execute()

        return {
            "msg":"user registered successfully..",
            "register_user_data":payload
        }
@app.post("/login")
def login_function(payload:dict):
    res_obj_supabase=supabase_client_object.table("users").select("*").eq("email",payload["email"]).eq("password",payload["password"]).eq("role",payload["role"]).execute()

    return {
        "msg":"user logged_in successfully..",
        "obj_supabase":res_obj_supabase
        }
