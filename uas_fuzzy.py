def down(x, xmin, xmax):
    return (xmax - x) / (xmax - xmin)


def up(x, xmin, xmax):
    return (x - xmin) / (xmax - xmin)


class Pakaian():
    min = 40
    med = 60
    max = 80

    def sedikit(self, x):
        if x >= self.med:
            return 0
        elif x <= self.min:
            return 1
        else:
            return down(x, self.min, self.med)

    def sedang(self, x):
        if x >= self.max or x <= self.min:
            return 0
        elif self.min < x < self.med:
            return up(x, self.min, self.med)
        elif self.med < x < self.max:
            return down(x, self.med, self.max)
        else:
            return 1

    def banyak(self, x):
        if x >= self.max:
            return 1
        elif x <= self.med:
            return 0
        else:
            return up(x, self.med, self.max)


class Kekotoran():
    min = 40
    med = 50
    max = 60
    vmax = 70

    def rendah(self, x):
        if x <= self.min:
            return 1
        elif x >= self.med:
            return 0
        else:
            return down(x, self.min, self.med)

    def sedang(self, x):
        if x >= self.max or x <= self.min:
            return 0
        elif self.min < x < self.med:
            return up(x, self.min, self.med)
        elif self.med < x < self.max:
            return down(x, self.med, self.max)
        else:
            return 1

    def tinggi(self, x):
        if x >= self.vmax or x <= self.med:
            return 0
        elif self.med < x < self.max:
            return up(x, self.med, self.max)
        elif self.max < x < self.vmax:
            return down(x, self.max, self.vmax)
        else:
            return 1

    def sangat_tinggi(self, x):
        if x >= self.vmax:
            return 1
        elif x <= self.max:
            return 0
        else:
            return up(x, self.max, self.vmax)


class Putaran():
    min = 500
    max = 1200
    pakaian = 0
    kekotoran = 0

    def __init__(self, pakaian, kekotoran):
        self.pakaian = pakaian
        self.kekotoran = kekotoran

    def _lambat(self, a):
        return self.max - a*(self.max - self.min)

    def _cepat(self, a):
        return a*(self.max - self.min) + self.min

    def _inferensi(self):
        pakaian = Pakaian()
        kekotoran = Kekotoran()
        result = []

        # [R1] If Pakaian sedikit and Kekotoran rendah then Kecepatan lambat
        a1 = min(pakaian.sedikit(self.pakaian),
                 kekotoran.rendah(self.kekotoran))
        z1 = self._lambat(a1)
        result.append((a1, z1))

        # [R2] If Pakaian sedikit and Kekotoran sedang then Kecepatan lambat
        a2 = min(pakaian.sedikit(self.pakaian),
                 kekotoran.sedang(self.kekotoran))
        z2 = self._lambat(a2)
        result.append((a2, z2))

        # [R3] If Pakaian sedikit and Kekotoran tinggi then Kecepatan lambat
        a3 = min(pakaian.sedikit(self.pakaian),
                 kekotoran.tinggi(self.kekotoran))
        z3 = self._lambat(a3)
        result.append((a3, z3))

        # [R4] If Pakaian sedikit and Kekotoran sangat tinggi then Kecepatan cepat
        a4 = min(pakaian.sedikit(self.pakaian),
                 kekotoran.sangat_tinggi(self.kekotoran))
        z3 = self._cepat(a4)
        result.append((a4, z3))

        # [R5] If Pakaian sedang and Kekotoran rendah then Kecepatan lambat
        a5 = min(pakaian.sedang(self.pakaian),
                 kekotoran.rendah(self.kekotoran))
        z5 = self._lambat(a5)
        result.append((a5, z5))

        # [R6] If Pakaian sedang and Kekotoran sedang then Kecepatan lambat
        a6 = min(pakaian.sedang(self.pakaian),
                 kekotoran.sedang(self.kekotoran))
        z6 = self._lambat(a6)
        result.append((a6, z6))

        # [R7] If Pakaian sedang and Kekotoran tinggi then Kecepatan cepat
        a7 = min(pakaian.sedang(self.pakaian),
                 kekotoran.tinggi(self.kekotoran))
        z7 = self._cepat(a7)
        result.append((a7, z7))

        # [R8] If Pakaian sedang and Kekotoran sangat tinggi then Kecepatan cepat
        a8 = min(pakaian.sedang(self.pakaian),
                 kekotoran.sangat_tinggi(self.kekotoran))
        z8 = self._cepat(a8)
        result.append((a8, z8))

        # [R9] If Pakaian BANYAK and Kekotoran rendah then Kecepatan lambat
        a9 = min(pakaian.banyak(self.pakaian),
                 kekotoran.rendah(self.kekotoran))
        z9 = self._lambat(a9)
        result.append((a9, z9))

        # [R10] If Pakaian BANYAK and Kekotoran sedang then Kecepatan cepat
        a10 = min(pakaian.banyak(self.pakaian),
                  kekotoran.sedang(self.kekotoran))
        z10 = self._cepat(a10)
        result.append((a10, z10))

        # [R11] If Pakaian BANYAK and Kekotoran tinggi then Kecepatan cepat
        a11 = min(pakaian.banyak(self.pakaian),
                  kekotoran.tinggi(self.kekotoran))
        z11 = self._cepat(a11)
        result.append((a11, z11))

        # [R12] If Pakaian BANYAK and Kekotoran sangat tinggi then Kecepatan cepat
        a12 = min(pakaian.banyak(self.pakaian),
                  kekotoran.sangat_tinggi(self.kekotoran))
        z12 = self._cepat(a12)
        result.append((a12, z12))

        return result

    def defuzifikasi(self):
        data_inferensi =  self._inferensi()
        res_a_z = 0
        res_a = 0
        for data in data_inferensi:
            # data[0] = a
            # data[1] = z
            res_a_z += data[0] * data[1]
            res_a += data[0]
        return res_a_z/res_a


ptrn = Putaran(65, 56)
print(ptrn.defuzifikasi())
