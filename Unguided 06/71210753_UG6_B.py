from NodeMahasiswa import NodeMahasiswa

class DLLNC:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    def  isEmpty(self):
        if self.size == 0:
            print("size data :",self.size)
            print("data tidak ada isinya")
            
    def __len__(self):
        return self.size
    
    def addElementTail(self,nama,ipk):
        baru = NodeMahasiswa(nama,ipk)
        if self.size == 0:
            self.head = baru
            self.tail = baru
        else:
            self.tail._next = baru
            baru._prev = self.tail
            self.tail = baru
        print("data masuk tail")
        self.size = self.size + 1

    def deleteLast(self):
        if self.size == 1:
            self.head = None
            self.tail = None
        else:
            hapus =  self.tail
            self.tail = self.tail._prev
            hapus._prev = None
            self.tail._next = None
            print("# Data",hapus._element,"Terhapus #")
            del hapus
        self.size = self.size - 1
    def printAllDescending(self):
        bantu = self.tail
        print("===== Print Descending =====")
        while bantu != None:
            print("="*30)
            print("Nama:",bantu._element)
            print("ipk:",bantu._ipk)
            bantu = bantu._prev
    def rataIpk(self):
        ipk = 0
        size = 0
        helper = self.tail
        while helper != None:
            ipk = ipk + helper._ipk
            helper = helper._prev
            size += 1
        print("===== Rata-Rata IPK =====")
        print("Rata - Rata :",round(ipk/size,2))

DLLNC1 = DLLNC()
DLLNC1.addElementTail('Shalom',3.9)
DLLNC1.addElementTail('Nabilla',3.8)
DLLNC1.addElementTail('Kurniadi',3.7)
DLLNC1.addElementTail('Harris',3.6)
DLLNC1.printAllDescending()
DLLNC1.deleteLast()
DLLNC1.printAllDescending()
DLLNC1.rataIpk()