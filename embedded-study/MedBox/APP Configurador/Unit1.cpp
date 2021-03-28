//---------------------------------------------------------------------------

#include <vcl.h>
#pragma hdrstop

#include "Unit1.h"
//---------------------------------------------------------------------------
#pragma package(smart_init)
#pragma link "nrclasses"
#pragma link "nrcomm"
#pragma link "nrcommbox"
#pragma resource "*.dfm"
TForm1 *Form1;
//---------------------------------------------------------------------------
__fastcall TForm1::TForm1(TComponent* Owner)
        : TForm(Owner)
{
}
//---------------------------------------------------------------------------
void __fastcall TForm1::Button1Click(TObject *Sender)
{
        nrComm1->Active=true;
        AnsiString mensagem="";
        mensagem="[" + Edit1->Text;
        mensagem=mensagem + "," + Edit2->Text;
        mensagem=mensagem + "," + Edit3->Text;
        mensagem=mensagem + "," + Edit4->Text;
        mensagem=mensagem + "," + Edit5->Text;
         mensagem=mensagem + "," + nome_da_rede->Text;
        mensagem=mensagem + "," + MaskEdit1->Text;
        mensagem=mensagem + "," + MaskEdit2->Text;
        mensagem=mensagem + "," + MaskEdit3->Text;
        mensagem=mensagem + "]";
        nrComm1->SendString(mensagem);

}
//---------------------------------------------------------------------------






