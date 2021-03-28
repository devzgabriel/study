//---------------------------------------------------------------------------

#ifndef Unit1H
#define Unit1H
//---------------------------------------------------------------------------
#include <Classes.hpp>
#include <Controls.hpp>
#include <StdCtrls.hpp>
#include <Forms.hpp>
#include "nrclasses.hpp"
#include "nrcomm.hpp"
#include "nrcommbox.hpp"
#include <Mask.hpp>
//---------------------------------------------------------------------------
class TForm1 : public TForm
{
__published:	// IDE-managed Components
        TnrComm *nrComm1;
        TnrDeviceBox *nrDeviceBox1;
        TLabel *Label1;
        TEdit *Edit1;
        TLabel *Label2;
        TEdit *Edit2;
        TLabel *Label3;
        TEdit *Edit3;
        TLabel *Label4;
        TButton *Button1;
        TMemo *Memo1;
        TMaskEdit *nome_da_rede;
        TLabel *DNS;
        TLabel *Subrede;
        TLabel *Numero_de_caracteres;
        TEdit *Edit4;
        TLabel *Label5;
        TEdit *Edit5;
        TMaskEdit *MaskEdit1;
        TMaskEdit *MaskEdit2;
        TMaskEdit *MaskEdit3;
        void __fastcall Button1Click(TObject *Sender);
private:	// User declarations
public:		// User declarations
        __fastcall TForm1(TComponent* Owner);
};
//---------------------------------------------------------------------------
extern PACKAGE TForm1 *Form1;
//---------------------------------------------------------------------------
#endif
