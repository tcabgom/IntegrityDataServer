import asyncio
import websockets

#Función del servidor para manejar los mensajes recividos
async def handler(websocket, path):
    #Recoje el mensaje
    data = await websocket.recv()

    #Crea una respuesta
    reply = f"Data recieved as:  {data}!"
    #Opcional, es para que usted pueda ver en la terminal que respuesta va a dar
    print(reply)
    #Manda de vuelta la respuesta al cliente
    await websocket.send(reply)

#Función para arrancar el servidor
start_server = websockets.serve(handler, "localhost", 8000)
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()




