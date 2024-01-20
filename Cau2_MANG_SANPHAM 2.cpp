#include <stdio.h>
#include <string.h>
struct NGAY{
	int ngay,thang,nam;
};

struct SANPHAM{
	char MaSP[10];
	char TenSP[255];
	NGAY NgaySX;
	int SoNamBH;
};

SANPHAM dsSP[1000];

void quickSort(int left, int right);
void SanPhamHetHan(int n, int namHienTai);
void xuatSP(int n);
void nhapSP(int &n);
void xuat1SP(SANPHAM x);



int main(){
	int n;
	nhapSP(n);
	printf("%-10s| %-10s| %-10s | %-5s|\n","MaSP","TenSP",
				"NgaySX","SoNamBH");
	xuatSP(n);
	printf("\n\tSau khi sap xep:\n\n");
	quickSort(0,n-1);
	printf("%-10s| %-10s| %-10s | %-5s|\n","MaSP","TenSP",
				"NgaySX","SoNamBH");
	xuatSP(n);
	
	printf("\n\tCac san pham het han bao hanh\n\n");
	SanPhamHetHan(n,2023);
	
}
void quickSort(int left, int right){

	int i = left, j = right;
	SANPHAM tag = dsSP[(left+right)/2];
	do{
		while(strcmp(tag.MaSP,dsSP[i].MaSP) > 0) i++;
		while(strcmp(tag.MaSP,dsSP[j].MaSP) < 0) j--;
		if(i<=j){
			SANPHAM x = dsSP[i];
			dsSP[i] = dsSP[j];
			dsSP[j] = x;
			i++; j--;
		}
	}while(i<j);
	if(j > left) quickSort(left,j);
	if(i < right) quickSort(i,right);
	
}
void SanPhamHetHan(int n, int namHienTai){
	int timThay = 0;
	for(int i=0;i<n;i++){
		int namBH = dsSP[i].NgaySX.nam + dsSP[i].SoNamBH;
		if(namBH < namHienTai){
			xuat1SP(dsSP[i]);
			timThay =1;
		}
	}
	if(timThay==0){
		printf("Khong co san pham nao het han bao hanh");
	}
}





void nhapSP(int &n){
	printf("Nhap so luong san pham: ");
	scanf("%d",&n);
	SANPHAM x;
	for(int i=0;i<n;i++){
		fflush(stdin);
		int trungma = 0;
		printf("Nhap ma san pham: ");
		gets(x.MaSP);
		for(int j=0; j<i; j++){
			if(strcmp(x.MaSP,dsSP[j].MaSP)==0){
				printf("\n\tTrung ma san pham\n\n");
				trungma = 1; break;
			}
		}
		if(trungma){
			i--;
			continue;
		}
		printf("Nhap ten san pham: ");
		gets(x.TenSP);
		printf("Nhap ngay san xuat (dd/MM/yyyy): ");
		scanf("%d/%d/%d",&x.NgaySX.ngay,&x.NgaySX.thang,&x.NgaySX.nam);
		printf("Nhap so nam Bao Hanh: "); scanf("%d",&x.SoNamBH);
		dsSP[i] = x;
		
	}
}
void xuat1SP(SANPHAM x){
	printf("%-10s| %-10s| %-2d/%-2d/%-4d | %-5d  |\n",x.MaSP,x.TenSP,x.NgaySX.ngay,x.NgaySX.thang,x.NgaySX.nam,x.SoNamBH);
}
void xuatSP(int n){
	for(int i=0;i<n;i++){
		xuat1SP(dsSP[i]);
	}
	printf("\n");
}


