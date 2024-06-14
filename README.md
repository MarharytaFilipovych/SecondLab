Second Lab
# Теоретичні питання 

## Що таке власне значення і власний вектор матриці? Як вони обчислюються?

**Власний вектор** - це ненульовий вектор 𝑣, для якого виконується співвідношення Av=λv, де 𝜆 це певний скаляр;  це ненульовий вектор, який під дією лінійного перетворення, що задається матрицею 𝐴 не міняює напрямку, але може змінювати довжину на коефіцієнт 𝜆.
Матриця розмірами n*n має не більше n власних векторів, та власних значень, що відповідають їм.
**Власне значення** - це коефіцієнт, з яким відповідний власний вектор стискається або розтягується при трансформації.
**Av=λv
det(λI - A) = 0**

## Які властивості мають власні вектори симетричних матриць?

* Власні вектори, що відповідають різним власним значенням симетричної матриці, є ортогональними один до одного. Це означає, що їх скалярний добуток дорівнює нулю.
* Власні вектори можна нормалізувати таким чином, щоб їхні норми дорівнювали 1: 
* Власні вектори симетричної матриці утворюють базис у просторі, до якого вони належать. Це означає, що будь-який вектор в цьому просторі можна виразити як лінійну комбінацію власних векторів.
* Симетричні матриці є діагоналізованими за допомогою ортогонального перетворення, і власні вектори є ключовими елементами цього процесу.

## Які можуть бути недоліки використання PCA, і які стратегії можуть використовуватися для подолання цих недоліків? 

## Які переваги має діагоналізація матриці в криптографії? Як вона застосовується для шифрування та дешифрування повідомлень?

* Діагональні матриці значно простіші для обчислень. Коли матриця діагоналізована, операції, такі як піднесення до степеня або множення, стають менш обчислювально затратними, оскільки ми можемо працювати лише з діагональними елементами.
* Обернена діагональна матриця також є діагональною, і її елементи обчислюються як обернені значення елементів початкової матриці. Це значно спрощує процес обернення матриці, що є важливим у багатьох криптографічних алгоритмах.
* Власні вектори та власні значення можуть використовуватись для побудови криптографічних схем, де діагоналізація може допомогти в шифруванні та дешифруванні даних.
* Діагоналізація дозволяє легко аналізувати спектр (набір власних значень) матриці, що важливо для розуміння її властивостей, зокрема у криптографії, де власні значення можуть мати важливе значення.
* Діагоналізація приводить матрицю до більш простої форми, що може бути корисно для аналізу та розуміння структури матриці.



