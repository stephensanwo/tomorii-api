from pydantic import EmailStr
from fastapi_mail import FastMail, MessageSchema, ConnectionConfig
from schema.Users import User


async def send_mail(email: EmailStr):

    template = """
        <html>
        <body>
          
        <p>Hi !!!
        <br>Thanks for using fastapi mail, keep using it..!!!</p>
  
        </body>
        </html>
        """

    message = MessageSchema(
        subject="Fastapi-Mail module",
        # List of recipients, as many as you can pass
        recipients=email.dict().get("email"),
        body=template,
        subtype="html"
    )

    fm = FastMail(conf)
    await fm.send_message(message)
    print(message)

    return JSONResponse(status_code=200, content={"message": "email has been sent"})
