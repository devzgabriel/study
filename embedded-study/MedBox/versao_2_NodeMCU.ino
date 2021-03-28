/*
    The server will set a GPIO pin depending on the request
      http://server_ip/gpio/0 will set the GPIO2 low,
      http://server_ip/gpio/1 will set the GPIO2 high
*/

#include <ESP8266WiFi.h>

#define travaa 15
#define travab 12
#define travac 13
#define travad 14
int hora = 3600000;

unsigned long intervaloa = 0;
unsigned long timeanta = 0;

unsigned long intervalob = 0;
unsigned long timeantb = 0;

unsigned long intervaloc = 0;
unsigned long timeantc = 0;

unsigned long intervalod = 0;
unsigned long timeantd = 0;
/*
#define ETE

#ifdef ETE
  #define STASSID "ETE-ALUNOS"
  #define STAPSK  "etefmc123"                                    NÃO É NECESSÁRIO MAS VOU PERGUNTAR A FUNÇÃO
  #endif
#else
  #define STASSID "MINHA_CASA"
  #define STAPSK  "senhadarede"                                    NÃO É NECESSÁRIO MAS VOU PERGUNTAR A FUNÇÃO
#endif
*/

/*IPAddress ip( ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? );
IPAddress gateway( ?? ?? ?? ?? ?? ?? ?? ?? ? );
IPAddress subnet( ?? ?? ?? ?? ?? ?? ?? ?? ?? );
IPAddress dns( ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ? );*/
const char* ssid = "Vanilda";
const char* password = "939vmlmm";
WiFiServer server(80);

void setup() {
  Serial.begin(9600);
  Serial.println();
  Serial.println();
  Serial.print(("Connecting to "));
  Serial.println(ssid);

  //WiFi.mode(WIFI_STA);
 // WiFi.config(ip, dns, gateway, subnet);
  WiFi.begin(ssid, password);

  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(F("."));
  }

  Serial.println();
  Serial.println(F("WiFi connected"));
  server.begin();
  Serial.print(F("Server started: "));
  Serial.println(WiFi.localIP());
}

void loop() {
  unsigned long timeatual = millis();
  WiFiClient client = server.available();           //Cria um cliente que pode se conectar a um endereço IP e porta IP da Internet especificados, conforme definido em client.connect () .
  //Obtém um cliente que está conectado ao servidor e tem dados disponíveis para leitura.
  if (!client) {
    return;
  }
  // while(!client.available){
  //   delay(1)                                      outra resposta p mesma situação
  //   }
  Serial.println(("new client"));

  client.setTimeout(5000); // default is 1000

  String req = client.readStringUntil('\r');
  Serial.println(("request: "));
  Serial.println(req);

  if (req.indexOf(("/gavetaa")) != -1) {                 //leitura do endereço para definir as horas
    if (req.indexOf(("/1")) != -1) {
      intervaloa = 1;
    }
    else if (req.indexOf(("/2")) != -1) {
      intervaloa = 2;
    }
    else if (req.indexOf(("/3")) != -1) {
      intervaloa = 3;
    }
    else if (req.indexOf(("/4")) != -1) {
      intervaloa = 4;
    }
    else if (req.indexOf(("/5")) != -1) {
      intervaloa = 5;
    }
    else if (req.indexOf(("/6")) != -1) {
      intervaloa = 6;
    }
    else if (req.indexOf(("/7")) != -1) {
      intervaloa = 7;
    }
    else if (req.indexOf(("/8")) != -1) {
      intervaloa = 8;
    }
    else if (req.indexOf(("/9")) != -1) {
      intervaloa = 9;
    }
    else if (req.indexOf(("/10")) != -1) {
      intervaloa = 10;
    }
    else if (req.indexOf(("/11")) != -1) {
      intervaloa = 11;
    }
    else if (req.indexOf(("/12")) != -1) {
      intervaloa = 12;
    }
    intervaloa = intervaloa * hora;
  }
  if (req.indexOf(("/gavetab")) != -1) {
    if (req.indexOf(("/1")) != -1) {
      intervalob = 1;
    }
    else if (req.indexOf(("/2")) != -1) {
      intervalob = 2;
    }
    else if (req.indexOf(("/3")) != -1) {
      intervalob = 3;
    }
    else if (req.indexOf(("/4")) != -1) {
      intervalob = 4;
    }
    else if (req.indexOf(("/5")) != -1) {
      intervalob = 5;
    }
    else if (req.indexOf(("/6")) != -1) {
      intervalob = 6;
    }
    else if (req.indexOf(("/7")) != -1) {
      intervalob = 7;
    }
    else if (req.indexOf(("/8")) != -1) {
      intervalob = 8;
    }
    else if (req.indexOf(("/9")) != -1) {
      intervalob = 9;
    }
    else if (req.indexOf(("/10")) != -1) {
      intervalob = 10;
    }
    else if (req.indexOf(("/11")) != -1) {
      intervalob = 11;
    }
    else if (req.indexOf(("/12")) != -1) {
      intervalob = 12;
    }
    intervalob = intervalob * hora;
  }
  if (req.indexOf(("/gavetac")) != -1) {
    if (req.indexOf(("/1")) != -1) {
      intervaloc = 1;
    }
    else if (req.indexOf(("/2")) != -1) {
      intervaloc = 2;
    }
    else if (req.indexOf(("/3")) != -1) {
      intervaloc = 3;
    }
    else if (req.indexOf(("/4")) != -1) {
      intervaloc = 4;
    }
    else if (req.indexOf(("/5")) != -1) {
      intervaloc = 5;
    }
    else if (req.indexOf(("/6")) != -1) {
      intervaloc = 6;
    }
    else if (req.indexOf(("/7")) != -1) {
      intervaloc = 7;
    }
    else if (req.indexOf(("/8")) != -1) {
      intervaloc = 8;
    }
    else if (req.indexOf(("/9")) != -1) {
      intervaloc = 9;
    }
    else if (req.indexOf(("/10")) != -1) {
      intervaloc = 10;
    }
    else if (req.indexOf(("/11")) != -1) {
      intervaloc = 11;
    }
    else if (req.indexOf(("/12")) != -1) {
      intervaloc = 12;
    }
    intervaloc = intervaloc * hora;
  }
  if (req.indexOf(("/gavetad")) != -1) {
    if (req.indexOf(("/1")) != -1) {
      intervalod = 1;
    }
    else if (req.indexOf(("/2")) != -1) {
      intervalod = 2;
    }
    else if (req.indexOf(("/3")) != -1) {
      intervalod = 3;
    }
    else if (req.indexOf(("/4")) != -1) {
      intervalod = 4;
    }
    else if (req.indexOf(("/5")) != -1) {
      intervalod = 5;
    }
    else if (req.indexOf(("/6")) != -1) {
      intervalod = 6;
    }
    else if (req.indexOf(("/7")) != -1) {
      intervalod = 7;
    }
    else if (req.indexOf(("/8")) != -1) {
      intervalod = 8;
    }
    else if (req.indexOf(("/9")) != -1) {
      intervalod = 9;
    }
    else if (req.indexOf(("/10")) != -1) {
      intervalod = 10;
    }
    else if (req.indexOf(("/11")) != -1) {
      intervalod = 11;
    }
    else if (req.indexOf(("/12")) != -1) {
      intervalod = 12;
    }
    intervalod = intervalod * hora;
  }
  client.flush();
  if (timeatual - timeanta > intervaloa and intervaloa != 0) {                        //Vamos escrever aqui sobre as solenoides
    timeanta = timeatual;
    digitalWrite(travaa, HIGH);
    delay(200);
    digitalWrite(travaa, LOW);
  }
  if (timeatual - timeantb > intervalob and intervalob != 0) {
    timeantb = timeatual;
    digitalWrite(travab, HIGH);
    delay(200);
    digitalWrite(travab, LOW);
  }
  if (timeatual - timeantc > intervaloc and intervaloc != 0) {
    timeantc = timeatual;
    digitalWrite(travac, HIGH);
    delay(200);
    digitalWrite(travac, LOW);
  }
  if (((timeatual - timeantd) > intervalod) && (intervalod != 0)) {
    timeantd = timeatual;
    digitalWrite(travad, HIGH);
    delay(200);
    digitalWrite(travad, LOW);
  }
  while (client.available()) {
    client.read();                     //Leia o próximo byte recebido do servidor ao qual o cliente está conectado (após a última chamada para read ())
  }
  client.println("HTTP/1.1 200 OK");
  client.println("Content-Type: text/html");
  client.println("");
  client.println("<!DOCTYPE HTML>\r\n<html>\r\n");
  client.println("Não utilize o navegador para acessar o MedBox,estamos trabalhando para uma solução em navegadores.\r\n Utilize o aplicativo por enquanto :)");
  client.println("</html>\r\n");

  /* o que é realmente necessario?
    client.print(F("HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n<!DOCTYPE HTML>\r\n<html>\r\n "));
    client.print((val) ? F("high") : F("low"));
    client.print(("<br><br>Click <a href='http://"));                         //neagle algorithm é usado para mandar pacotes maiores em TCP/IP
    client.print(WiFi.localIP());
    client.print(("/gpio/1'>here</a> to switch LED GPIO on, or <a href='http://"));
    client.print(WiFi.localIP());
    client.print(F("/gpio/0'>here</a> to switch LED GPIO off.</html>"));
  */
}
