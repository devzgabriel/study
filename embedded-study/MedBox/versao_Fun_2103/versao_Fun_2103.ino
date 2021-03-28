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

String ssid = "PROJETE";//ETE-CURSOS
String password = "prjt2019";//987etefmc321
String ips;
String gateways;
String subnets;
IPAddress ip (192, 168, 20, 45);
IPAddress gateway(192, 168, 20, 1);
IPAddress subnet(255, 255, 255, 0);
IPAddress dns(1, 1, 1, 1);
WiFiServer server(80);

String mensagem = "";
char rx;
int num_vig = 0;
int num_pass = 0;

void setup() {

  pinMode(travaa, OUTPUT);
  pinMode(travab, OUTPUT);
  pinMode(travac, OUTPUT);
  pinMode(travad, OUTPUT);

  delay(1000);
  Serial.begin(9600);
  Serial.println();
  Serial.println();
/*  if (digitalRead(D2) == 0)
  {
    //Modo de configuracao
    Serial.println("Configurando o dispositivo");
    rx = 0;
    while (rx != ']')
    {
      if (Serial.available())
      {
        rx = Serial.read();
        if (rx == '[') mensagem = "";
        else if (rx != ']') mensagem = mensagem + rx;
      }
    }
    //Split

    //nome_rede,senha_rede,ip,gateway,subnet
    num_vig = mensagem.indexOf(",");
    ssid = mensagem.substring(1, num_vig);
    mensagem = mensagem.substring(num_vig + 1, mensagem.length());
    Serial.print(ssid);
    num_vig = mensagem.indexOf(",");
    password = mensagem.substring(1, num_vig);
    mensagem = mensagem.substring(num_vig + 1, mensagem.length());
    Serial.print(password);
    num_vig = mensagem.indexOf(",");
    ips = mensagem.substring(1, num_vig);
    mensagem = mensagem.substring(num_vig + 1, mensagem.length());
    Serial.print(ips);
    num_vig = mensagem.indexOf(",");
    gateways = mensagem.substring(1, num_vig);
    mensagem = mensagem.substring(num_vig + 1, mensagem.length());
    Serial.print(gateways);
    num_vig = mensagem.indexOf(",");
    subnets = mensagem.substring(1, num_vig);
    mensagem = mensagem.substring(num_vig + 1, mensagem.length());
    Serial.print(subnets);


    IPAddress ip = ip.fromString(ips);
    IPAddress gateway = gateway.fromString(gateways);
    IPAddress subnet = subnet.fromString(subnets);
    Serial.print("ip>>>>");
    Serial.println(ip);
    Serial.print("gateway>>>>");
    Serial.println(gateway);
    Serial.print("subnet>>>>");
    Serial.println(subnet);

    //Envia para confirmar
    Serial.println("Rede configurada:");
  }*/
  Serial.print(("Connecting to "));
  Serial.println(ssid);

  WiFi.config(ip, dns, gateway, subnet);
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

  if (timeatual - timeanta > intervaloa && intervaloa != 0) {                        //Vamos escrever aqui sobre as solenoides
    timeanta = timeatual;
    digitalWrite(travaa, HIGH);
    delay(200);
    digitalWrite(travaa, LOW);
    Serial.println(timeanta);
    Serial.println("Gaveta 1 ativa");
  }
  if (timeatual - timeantb > intervalob && intervalob != 0) {
    timeantb = timeatual;
    digitalWrite(travab, HIGH);
    delay(200);
    digitalWrite(travab, LOW);
    Serial.println(timeantb);
    Serial.println("Gaveta 2 ativa");
  }
  if (timeatual - timeantc > intervaloc && intervaloc != 0) {
    timeantc = timeatual;
    digitalWrite(travac, HIGH);
    delay(200);
    digitalWrite(travac, LOW);
    Serial.println(timeantc);
    Serial.println("Gaveta 3 ativa");
  }
  if (((timeatual - timeantd) > intervalod) && (intervalod != 0)) {
    timeantd = timeatual;
    digitalWrite(travad, HIGH);
    delay(200);
    digitalWrite(travad, LOW);
    Serial.println(timeantd);
    Serial.println("Gaveta 4 ativa");
  }

  if (!client) {
    return;
  }
  Serial.println(("new client"));

  client.setTimeout(5000); // default is 1000

  String req = client.readStringUntil('\r');
  Serial.println(("request: "));
  Serial.println(req);

  if (req.indexOf(("/gavetaa")) != -1) {                 //leitura do endereço para definir as horas
    if (req.indexOf(("gavetaa/0")) != -1) {
      intervaloa = 0;
    }
    else if (req.indexOf(("gavetaa/1")) != -1) {
      intervaloa = 1;
    }
    else if (req.indexOf(("gavetaa/2")) != -1) {
      intervaloa = 2;
    }
    else if (req.indexOf(("gavetaa/3")) != -1) {
      intervaloa = 3;
    }
    else if (req.indexOf(("gavetaa/4")) != -1) {
      intervaloa = 4;
    }
    else if (req.indexOf(("gavetaa/5")) != -1) {
      intervaloa = 5;
    }
    else if (req.indexOf(("gavetaa/6")) != -1) {
      intervaloa = 6;
    }
    else if (req.indexOf(("gavetaa/7")) != -1) {
      intervaloa = 7;
    }
    else if (req.indexOf(("gavetaa/8")) != -1) {
      intervaloa = 8;
    }
    else if (req.indexOf(("gavetaa/9")) != -1) {
      intervaloa = 9;
    }
    else if (req.indexOf(("gavetaa/10")) != -1) {
      intervaloa = 10;
    }
    else if (req.indexOf(("gavetaa/11")) != -1) {
      intervaloa = 11;
    }
    else if (req.indexOf(("gavetaa/12")) != -1) {
      intervaloa = 12;
    }
    timeanta = timeatual;
    intervaloa = intervaloa * 10000;
    Serial.print(intervaloa);
  }
  if (req.indexOf(("/gavetab")) != -1) {
    if (req.indexOf(("gavetab/0")) != -1) {
      intervaloa = 0;
    }
    else if (req.indexOf(("gavetab/1")) != -1) {
      intervalob = 1;
    }
    else if (req.indexOf(("gavetab/2")) != -1) {
      intervalob = 2;
    }
    else if (req.indexOf(("gavetab/3")) != -1) {
      intervalob = 3;
    }
    else if (req.indexOf(("gavetab/4")) != -1) {
      intervalob = 4;
    }
    else if (req.indexOf(("gavetab/5")) != -1) {
      intervalob = 5;
    }
    else if (req.indexOf(("gavetab/6")) != -1) {
      intervalob = 6;
    }
    else if (req.indexOf(("gavetab/7")) != -1) {
      intervalob = 7;
    }
    else if (req.indexOf(("gavetab/8")) != -1) {
      intervalob = 8;
    }
    else if (req.indexOf(("gavetab/9")) != -1) {
      intervalob = 9;
    }
    else if (req.indexOf(("gavetab/10")) != -1) {
      intervalob = 10;
    }
    else if (req.indexOf(("gavetab/11")) != -1) {
      intervalob = 11;
    }
    else if (req.indexOf(("gavetab/12")) != -1) {
      intervalob = 12;
    }
    timeantb = timeatual;
    intervalob = intervalob * 10000;
    Serial.print(intervalob);
  }
  if (req.indexOf(("/gavetac")) != -1) {
    if (req.indexOf(("gavetac/0")) != -1) {
      intervaloa = 0;
    }
    else if (req.indexOf(("gavetac/1")) != -1) {
      intervaloc = 1;
    }
    else if (req.indexOf(("gavetac/2")) != -1) {
      intervaloc = 2;
    }
    else if (req.indexOf(("gavetac/3")) != -1) {
      intervaloc = 3;
    }
    else if (req.indexOf(("gavetac/4")) != -1) {
      intervaloc = 4;
    }
    else if (req.indexOf(("gavetac/5")) != -1) {
      intervaloc = 5;
    }
    else if (req.indexOf(("gavetac/6")) != -1) {
      intervaloc = 6;
    }
    else if (req.indexOf(("gavetac/7")) != -1) {
      intervaloc = 7;
    }
    else if (req.indexOf(("gavetac/8")) != -1) {
      intervaloc = 8;
    }
    else if (req.indexOf(("gavetac/9")) != -1) {
      intervaloc = 9;
    }
    else if (req.indexOf(("gavetac/10")) != -1) {
      intervaloc = 10;
    }
    else if (req.indexOf(("gavetac/11")) != -1) {
      intervaloc = 11;
    }
    else if (req.indexOf(("gavetac/12")) != -1) {
      intervaloc = 12;
    }
    timeantc = timeatual;
    intervaloc = intervaloc * 10000;
    Serial.print(intervaloc);
  }
  if (req.indexOf(("/gavetad")) != -1) {
    if (req.indexOf(("gavetad/0")) != -1) {
      intervaloa = 0;
    }
    else if (req.indexOf(("gavetad/1")) != -1) {
      intervalod = 1;
    }
    else if (req.indexOf(("gavetad/2")) != -1) {
      intervalod = 2;
    }
    else if (req.indexOf(("gavetad/3")) != -1) {
      intervalod = 3;
    }
    else if (req.indexOf(("gavetad/4")) != -1) {
      intervalod = 4;
    }
    else if (req.indexOf(("gavetad/5")) != -1) {
      intervalod = 5;
    }
    else if (req.indexOf(("gavetad/6")) != -1) {
      intervalod = 6;
    }
    else if (req.indexOf(("gavetad/7")) != -1) {
      intervalod = 7;
    }
    else if (req.indexOf(("gavetad/8")) != -1) {
      intervalod = 8;
    }
    else if (req.indexOf(("gavetad/9")) != -1) {
      intervalod = 9;
    }
    else if (req.indexOf(("gavetad/10")) != -1) {
      intervalod = 10;
    }
    else if (req.indexOf(("gavetad/11")) != -1) {
      intervalod = 11;
    }
    else if (req.indexOf(("gavetad/12")) != -1) {
      intervalod = 12;
    }
    timeantb = timeatual;
    intervalod = intervalod * 10000;
    Serial.print(intervalod);
  }

  while (client.available()) {
    client.read();                     //Leia o próximo byte recebido do servidor ao qual o cliente está conectado (após a última chamada para read ())
  }
  client.println("HTTP/1.1 200 OK");
  client.println("Content-Type: text/html");
  client.println("");
  client.println("<!DOCTYPE HTML>\r\n<html>\r\n");
  client.println("Nao utilize o navegador para acessar o MedBox,estamos trabalhando para uma solucao em navegadores.\r\n Utilize o aplicativo por enquanto :)");
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
