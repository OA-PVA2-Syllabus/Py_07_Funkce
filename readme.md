# PVA2 - Programování a vývoj aplikací
## Cvičení 09: Funkce

### 1
Deklarujte funkce `hello`, která vypíše text `Hello world`.

### 2
Pomocí cyklu použijte funkci `hello` 5krát. tzn. text `hello world` bude vypsán pětkrát.

### 3 
Deklarujte funkci `showHello`, jenž bude mít vstupní parametr count. Vstupním parametrem count budete určovat, kolikrát se funkce hello zavolá a vypíše výstupní hodnota. 
Použijte funkci showHello s argumentem dle uvážení

### 4
Definujte funkci `square`, jenž bude vracet vypočítanou hodnotu druhé mocniny zadané do vstupního parametru.

Vyzkoušejte zavolat druhé mocniny čísel 4, 8, 15, 23, -1

### 5
a) Pomocí funkce `sumOfTwo`, vytvořte součet dvou čísel. Uvnitř fce využijte vhodně funkci return.

b) Sečtěte dvakrát výsledek volání funkce `sumOfTwo` a výsledek zobrazte uživateli. Každé volání fce bude mít jiné argumenty.


### 6
Sestavte funkci `multiply`, jenž bude obsahovat tři parametry a, b, c. Nastavte výchozí hodnotu parametru b na 2 a c na 10. Funkce bude vracet provádět matematickou operaci a násobí b a přičítá c.

### 7
`barvy = ["red", "green", "blue", "white"]`

Napište funkci 'add_unique', která jako vstup přijme seznam a prvek. Funkce přidá prvek do seznamu pouze v případě, že se v seznamu ještě nenachází.

### 8
`barvy = ["red", "green", "blue", "white", "red", "black", "orange", "black"]`

Deklarujte funkci remove_duplicates, která přijme na vstupu seznam řetězců a vrátí nový seznam obsahující pouze unikátní prvky ze vstupního seznamu.

### 9
Sestavte funkci `listsum`, které pomocí parametru předáte seznam čísel. Funkce spočítá a vypíše součet čísel v seznamu, která jsou kladná, nebo jsou menší než -10.

Například pro seznam `-12, -11, -10, -9, 0, 1, 2, 3` bude výstup programu vypadat následovně:

Součet čísel, která jsou kladná, nebo jsou menší než -10 je -17.

Vytvořte dvě proměnné a uložte do nich dva seznamy:
* `-14, -12, -10, 1, 2, 3`
* `1,1,1, -11, -11, -11`

Vyzkoušete funkci pro oba seznamy.

### 10
Sestavte funkci `faktorial`, která bude vracet hodnotu faktoriálu zadaného v argumentu. Výsledek faktoriálu zobrazte uživateli.

### 11
Napište funkci, která přijme na vstup slovo a vrátí jeho vypočtenou "hodnotu" na základě následujících pravidel:
- Souhlásky mají hodnotu 1 bodu.
- Samohlásky mají hodnotu 3 bodů.
- Písmeno "x" má hodnotu 10 bodů.
- Všechny ostatní znaky mají hodnotu 0 bodů.
