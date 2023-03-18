from  flask  import  Flask , request , jsonify

app  =  "Frasco" ( __name__ )

@ app . rota ( '/' )
def índex():
  resultado  =  "None"
  mídia  =  "None"      

  nota1  = request.args.get('nota1')
  nota2  = request.args.get('nota2')

  if  nota1  and  nota2:
    nota1  =  float( nota1 )
    nota2  =  float( nota2 )

  mídia  = ( nota1  +  nota2 ) /  2
  
  return jsonify( mídia )

if __name__  ==  "__main__":
  app . run (host = '0.0.0.0' , porta = 5000)