### Как хеширование помогает обеспечивать безопасность блокчейна

Хеширование — это ключевая технология, которая делает блокчейн устойчивым к изменениям и обеспечивает его безопасность. Вот основные аспекты:

---

#### 1. **Целостность данных**
Хеширование используется для создания уникального идентификатора каждого блока на основе его содержимого:
- Каждый блок содержит хеш предыдущего блока, что связывает блоки в единую цепочку.
- Если данные в каком-либо блоке изменяются, его хеш становится другим, что нарушает цепочку.

Это позволяет сразу обнаружить любые изменения в данных.

---

#### 2. **Неизменяемость блокчейна**
Хеш-функции (например, SHA-256) обладают следующими свойствами:
- **Детерминированность:** один и тот же ввод всегда даёт одинаковый вывод.
- **Устойчивость к коллизиям:** вероятность того, что два разных ввода дадут один и тот же хеш, крайне мала.
- **Однонаправленность:** невозможно восстановить оригинальные данные по их хешу.

Эти свойства делают практически невозможным изменение данных без изменения всей цепочки блоков.

---

#### 3. **Защита от атак**
- **Proof of Work (PoW):** Майнеры должны найти хеш с определёнными характеристиками (например, начинающийся с определённого числа нулей). Это требует значительных вычислительных ресурсов, что делает атаки на сеть дорогостоящими.
- **Устойчивость к хеш-коллизиям:** Даже минимальное изменение данных приводит к полностью новому хешу, что усложняет подделку блоков.

---

#### 4. **Быстрая проверка данных**
Хеширование позволяет быстро проверить целостность и подлинность данных. Например:
- Узлы могут проверять, что данные транзакции в блоке не были изменены.
- Пользователи могут убедиться, что полученные данные соответствуют оригиналу.

---

#### Пример:
Если злоумышленник попытается изменить транзакцию в одном блоке, это изменит хеш этого блока. Поскольку следующий блок содержит хеш предыдущего блока, его хеш тоже станет недействительным. Чтобы скрыть изменения, злоумышленнику пришлось бы пересчитать все хеши в цепочке, что практически невозможно в больших сетях.

---

Таким образом, хеширование защищает блокчейн, обеспечивая целостность, неизменяемость данных и устойчивость к атакам. Это фундаментальная технология, которая делает блокчейн надёжным инструментом для хранения данных и выполнения транзакций.