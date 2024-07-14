# Maths

This section is dedicated to the mathematical concepts that are commonly used in competitive programming. The section is divided into three subsections: Numeric Systems, Number Theory, Algebra and Geometry.

## 1-Numeric Systems

The purpose of this section is to make brief introduction to numerical system. We give an special attention to the binary system, since it is the most used in competitive programming. The script includes a brief explanation of the binary system and its applications in problem-solving.

## Basic Concepts

In the simplest generalization of the decimal numeric system, any positional numeric system is defined firstly by a number $b$, called the base. That base indicates the number of digits used in the representation. Secondly, the positional numeric system is defined by the set of digits, which are the numbers from $0$ to $b-1$. The notation of a number being in base $b$ is written as $(d_nd_{n-1}...d_2d_1d_0)_b$, with $0\le d_i < b$. The mathematical rule definition of a number in base $b$ is given by:
$$(d_nd_{n-1}...d_2d_1d_0)_b=\sum_{i=0}^{n}d_ib^i$$

By example the number $(123)_8$ in base $8$ is equal to $1\cdot8^2+2\cdot8^1+3\cdot8^0=83$ in base $10$. The number $(1011)_2$ in base $2$ is equal to $1\cdot2^3+0\cdot2^2+1\cdot2^1+1\cdot2^0=11$ in base $10$.

### Conversion between bases

The conversion between bases is a simple process. To convert a number from base $b$ to base $10$, we use the formula above. To convert a number from base $10$ to base $b$, we divide the number by $b$ and store the remainder. We repeat the process with the quotient until the quotient is zero, finally the representation is given by the remainders in reverse order.

 Python already has a built-in function to convert numbers between bases. The function `int(str, base)` converts the string `str` representing an integer in base `base` to base 10. The function `bin(n)`, `oct(n)`, and `hex(n)` convert the integer `n` to a string in binary, octal, and hexadecimal, respectively. So the function `int(str, base)` is the inverse of `bin(n)`, `oct(n)`, and `hex(n)`. The script includes a problem where we need to use a custom function to convert a number from base $10$ to base $25$.

### Binary System in Competitive Programming

The stright forward way of using the binary system modeling a collection of $n$ objects with binary states. In the model, the $i$-th object is represented by the $i$-th bit of a binary number that we call $bmodel$. The state of the object is represented by the value of the bit, $0$ for off and $1$ for on. Then for an object we can check if it is on or off, turn it on or off, or toggle its status as follows:

1. Check if the $i$-th object is on: $(bmodel)\text{AND}(1<<i)$.
2. Turn on the $i$-th object: $(bmodel)\text{OR}(1<<i)$.
3. Turn off the $i$-th object: $(bmodel)\text{AND}(\sim(1<<i))$.
4. Toggle the $i$-th object: $(bmodel)\text{XOR}(1<<i)$.
5. Turn on all objects: $(1<<n)-1$.

The script includes a code using the mentioned model to enumerate all the subsets of a set of $n$ elements.

### Useful numbers and operations

**Floor function**: The floor function $\lfloor x\rfloor$ is the greatest integer less than or equal to $x$, and is defined as $\lfloor x\rfloor=\max\{n\in\mathbb{Z}:n\le x\}$. This function satisfies that $\lfloor x\rfloor\le x<\lfloor x\rfloor+1$.

**Ceiling function**: The ceiling function $\lceil x\rceil$ is the smallest integer greater than or equal to $x$, and is defined as $\lceil x\rceil=\min\{n\in\mathbb{Z}:n\ge x\}$. This one satisfies that $\lceil x\rceil-1<x\le\lceil x\rceil$.

**Truncation**: The truncation function $\text{trunc}(x)$ is the integer part of $x$, and is defined as $\text{trunc}(x)=\lfloor x\rfloor$ if $x\ge0$ and $\text{trunc}(x)=\lceil x\rceil$ if $x<0$.

**Harmonic Numbers**: The $n$-th harmonic number is defined as $H_n=\displaystyle\sum_{i=1}^{n}\dfrac{1}{i}$. Using the lower and upper Darboux sums, we can get some useful inequalities for $H_n$. Remember that Darboux sum are defined as:

$$L_n=\displaystyle\sum_{i=1}^{n-1}\inf_{[x_i, x_{i+1}]}f(x)\cdot \Delta x$$

$$U_n=\displaystyle\sum_{i=1}^{n-1}\sup_{[x_i, x_{i+1}]}f(x)\cdot \Delta x$$

Consider the function $f(x)=\dfrac{1}{x}$ for $x\in[1,n]$. If we use the partition of $[1,n]$ where $\Delta x=1$, then the Darboux sums for $f$ are given by:

$$L_n=\displaystyle\sum_{i=1}^{n-1}\dfrac{1}{i+1}=\dfrac{1}{2}+\dfrac{1}{3}+...+\dfrac{1}{n} = H_n-1$$

$$U_n=\displaystyle\sum_{i=1}^{n-1}\dfrac{1}{i}=\dfrac{1}{1}+\dfrac{1}{2}+...+\dfrac{1}{n-1} = H_{n-1}$$

The area $A_f$ under the curve of $1/x$ is:
$$A_f = \int_{1}^{n}\dfrac{1}{x}dx=\ln(n)$$

Since the area under the curve can be sandwiched between the lower and upper Darboux sums, we get the following inequalities:
$$H_{n}-1\le\ln(n)\le H_{n-1}$$

Harmonic numbers and the presented functions are useful in the analysis of algorithms as we'll see in the next sections.

## 2-Number Theory

### Divisibility

An integer m is a divisor of an integer n if there exists an integer k such that $n=km$, and we write $m|n$. When $m$ does not divide $n$ we write $m\nmid n$, and the remainder is denoted as $n\mod m$. The set of all divisors of an integer n is denoted by $D_n$. The number of divisors of n is denoted by $D_n$.

We say that q is a common divisor of m and n if $q|m$ and $q|n$. The greatest common divisor of m and n is the largest integer that divides both $m$ and $n$, and is denoted by $gcd(m,n)$. It is easy to prove that $gcd(m,n,p)=gcd(gcd(m,n),p)$. By induction we can show that if $m_1,m_2,...,m_k\in\mathbb{Z}$, then

$$gcd(m_1,m_2,...,m_k)=gcd(gcd(m_1,m_2,...,m_{k-1}),m_k)$$

The following theorem is fundamental in divisibility:

**Theorem 1 (Division Algorithm):** For any integers m and n, with $m>0$, there exist unique integers q and r such that $n=qm+r$ and $0\le r<m$.

Next we enumerate some properties of the greatest common divisor of two integers $m,n\in\mathbb{Z}$:

**Proposition 1:** There exists integers $x,y\in\mathbb{Z}$ such that $gcd(m,n)=mx+ny$.

**Proposition 2:** If $q|n$ and $q|n$, then $gcd\bigg(\dfrac{m}{q},\dfrac{n}{q}\bigg)=\dfrac{1}{q}gcd(m,n)$.

**Proposition 3:** If $gcd(q,m)=gcd(q,n)=1$, then $gcd(q,mn)=1$.

How can $gcd$ be found? The Euclidean algorithm is a method to find the greatest common divisor of two integers. The algorithm is based on the following property of the greatest common divisor:

**Proposition 4:** If $m=nq+r$, then $gcd(m,n)=gcd(n,r)$.

**Theorem 1 (Euclidean Algorithm):** The greatest common divisor of two integers $m$ and $n$ can be found by the following recursive formula:
$$gcd(m,n)=\begin{cases}n & \text{if } m=0\\gcd(n,n\mod m) & \text{if } m\neq0\end{cases}$$

In the case where $gcd(n,m)=1$, we say that $n$ and $m$ are relatively prime. Some useful properties of relatively prime numbers are:

**Proposition 5:** If $q|mn$ and $gcd(q,m)=1$, then $q|n$.

### Primes

An integer $n$ is prime if it has exactly two divisors, $1$ and $n$. The set of all prime numbers is denoted by $\mathbb{P}$.

**Theorem 2 (Fundamental Theorem of Arithmetic):** Every integer $n>1$ can be uniquely represented as a product of prime numbers.
$$n=p_1^{\alpha_1}p_2^{\alpha_2}...p_k^{\alpha_k}$$

Note that if $n$ is a composite number, then it can be represented as $n = a\cdot b$, with $1 < a\le b < n$. That implies that $a\le\sqrt{n}$ (why). So, in the case of $a$ being prime or composite, we can always find a prime divisor of $n$ less than or equal to $\sqrt{n}$. The stright forward consecuence of this fact is that we can check if a number is prime in $O(\sqrt{n})$ by checking if it has a divisor less than or equal to its square root.

**Theorem 3 (Sieve of Eratosthenes):** The sieve of Eratosthenes is an algorithm that finds all prime numbers up to a given integer $n$. The algorithm works as follows:

1. Create a list of consecutive integers from $2$ through $n$: $(2,3,4,...,n)$.
2. Let $p$ equal $2$, the first prime number.
3. Enumerate the multiples of $p$ by counting in increments of $p$ from $2p$ to $n$, and mark them in the list.
4. Find the smallest number in the list greater than $p$ that is not marked. If there is no such number, stop. Otherwise, let $p$ now equal this new number (which is the next prime), and repeat from step 3.
5. When the algorithm terminates, the unmarked numbers in the list are all the prime numbers below $n$.

We can adapt the sieve of Eratosthenes to find the divisors of all numbers from $1$ up to $n$ in $O(n\ln n)$ time. The idea consists of creating an array of size $n+1$, where slot $j$ stores the numbers of divisor of $j$. So for each $i$ we iterate over the multiples of $i$ and increment the number of divisors of the multiple by $1$. The script includes a code that implements the both sieves.

Finally we present a proof of the complexity of the adapted sieve of Eratosthenes, to see a stright forwad use of harmonic numbers in algorithm analysis:

 **Proof**: For each $i$ from 1 to $n$, we iterate over the multiples of $i$ a total of $\lfloor n/i\rfloor$ times. So the total number of iterations is given by:
$$\sum_{i=1}^{n}\lfloor n/i\rfloor\le n\sum_{i=1}^{n}\dfrac{1}{i}=nH_n\le n(\ln(n)+1)\sim n\ln(n)$$

So we conclude that the complexity of the adapted sieve of Eratosthenes is $O(n\ln n)$.

### Modular Arithmetic

The purpose of this section is to introduce fundamental concepts of congruences and remainders. We include a common application of modular arithmetic in competitive programming, the computation of large powers of numbers.

**Definition 1:** Let $a,b,n\in\mathbb{Z}$ with $n>0$. We say that $a$ is congruent to $b$ modulo $n$ if $n|(a-b)$, and we write $a\equiv b\text{ mod } n$. The set of all integers congruent to $a$ modulo $n$ is denoted by $[a]_n$.

We know that there exists $j,k\in\mathbb{N}$ such that
$a=nj+r_a$ and $b=nk+r_b$, $r_a<n,\ r_b<n$. If we substract both expressions then $a-b=n(j-k)+r_a-r_b$. If $a\equiv b\text{ mod } n$, then necessarily $r_a=r_b$. We can summarize this as follows:

**Proposition 6:** Let $a,b,n\in\mathbb{Z}$ with $n>0$. Then we have $a\equiv b\text{ mod } n$ if and only if $a\text{ mod } n=b\text{ mod } n$.

Some arithmetic properties of congruences are:

**Proposition 7:** Let $a,b,c,d,n\in\mathbb{Z}$ with $n>0$. Then:

1. $a\equiv b\text{ mod } n$ is equivalent to $b\equiv a\text{ mod } n$.
2. $a\equiv b\text{ mod } n$ and $b\equiv c\text{ mod } n$ implies $a\equiv c\text{ mod } n$.
3. $a\equiv b\text{ mod } n$ and $c\equiv d\text{ mod } n$ implies $a+c\equiv b+d\text{ mod } n$ and $ac\equiv bd\text{ mod } n$.
4. If $ax\equiv bx\text{ mod } n$, then $a\equiv b\text{ mod } \frac{n}{gcd(n,x)}$.

Due to the Division Theorem, for $a,n\in\mathbb{Z}$ with $n>0$, there exist unique integers $q$ and $r$ such that $a=nq+r$ and $0\le r<n$. Now this is $a\equiv r\text{ mod } n$. The remainder $r$ is called the residue of $a$ modulo $n$, and we denote it by $a\text{ mod } n$. This means that in modular arithmetic there is not distinction between the number and its residue, leading to the following properties:

**Proposition 8:** Let $a,b,n\in\mathbb{Z}$ with $n>0$. Then:

1. $(a+b)\text{ mod } n=((a\text{ mod } n)+(b\text{ mod } n))\text{ mod } n$.
2. $(a-b)\text{ mod } n=((a\text{ mod } n)-(b\text{ mod } n))\text{ mod } n$.
3. $(a\cdot b)\text{ mod } n=((a\text{ mod } n)\cdot(b\text{ mod } n))\text{ mod } n$.
4. $a^k\text{ mod } n=(a\text{ mod } n)^k\text{ mod } n$.

### More on Primes

The Euler totient function $\phi(n)$ is defined as the number of integers $k$ such that $1\le k\le n$ and $gcd(k,n)=1$. The Euler totient function satisfies the following properties:

**Proposition 9:** Let $m,n\in\mathbb{Z}$ with $m,n>0$. Then:

1. $\phi(mn)=\phi(m)\phi(n) \dfrac{d}{\phi(d)}$, where $d=\gcd(a,b)$.
2. If $m|n$, then $\phi(m)|\phi(n)$.
3. If $p$ is prime, then $\phi(p)=p-1$.
4. If $p$ is prime and $k\in\mathbb{N}$, then $\phi(p^k)=p^k-p^{k-1}$.
5. If $m,n\in\mathbb{N}$ are relatively prime, then $\phi(mn)=\phi(m)\phi(n)$.
6. If $n=p_1^{\alpha_1}p_2^{\alpha_2}...p_k^{\alpha_k}$, then $\phi(n)=n\prod_{i=1}^{k}\left(1-\dfrac{1}{p_i}\right)$.
7. **Gauss divisors sum theorem:** Let $n\in\mathbb{N}$. Then $\sum_{d|n}\phi(d)=n$.
Additional important results concerning primes are:

**Theorem 4 (Fermat's Little Theorem):** Let $p$ be a prime number and $a\in\mathbb{Z}$ with $p\nmid a$. Then $a^{p-1}\equiv 1\text{ mod } p$.

**Theorem 5 (Euler's Theorem):** Let $n\in\mathbb{N}$ and $a\in\mathbb{Z}$ with $gcd(a,n)=1$. Then $a^{\phi(n)}\equiv 1\text{ mod } n$.

**Theorem 6 (Wilson's Theorem):** Let $p$ be a prime number. Then $(p-1)!\equiv -1\text{ mod } p$.

**Definition 2:** Let $a,n\in\mathbb{Z}$ with $n>0$. The modular multiplicative inverse of $a$ modulo $n$ is an integer $x$ such that $ax\equiv 1\text{ mod } n$. We denote the modular multiplicative inverse of $a$ modulo $n$ by $a^{-1_n}$.

From Euler's theorem we can derive a formula to compute the modular multiplicative inverse of $a$ modulo $n$:

**Proposition 10:** Let $a,n\in\mathbb{Z}$ with $gcd(a,n)=1$. Then $a^{-1_n}=a^{\phi(n)-1}$.

### Groups

**Definition 3:** A group is a set $G$ with a binary operation $\cdot$ that satisfies the following properties:

1. **Closure:** For all $x,y\in G$, $x\cdot y\in G$.
2. **Associativity:** For all $x,y,z\in G$, $(x\cdot y)\cdot z=x\cdot(y\cdot z)$.
3. **Identity element:** There exists an element $e\in G$ such that for all $a\in G$, $x\cdot e=e\cdot x=x$.
4. **Inverse element:** For all $a\in G$, there exists an element $x^{-1}\in G$ such that $x\cdot x^{-1}=x^{-1}\cdot x=e$.

**Definition 3:** A group $G$ is abelian if for all $x,y\in G$, $x\cdot y=y\cdot x$.

If $x\in G$, we define $x^n$ as the product of $x$ by itself $n$ times. It is easy to verify the usual powers properties. The value $x^n$ can be computed efficiently in $O(\log_2n)$ using the following recursive formula:

$$x^n=\begin{cases}1 & \text{if } n=0\\x^{n/2}\cdot x^{n/2} & \text{if } n\text{ is even}\\x\cdot x^{(n-1)/2}\cdot x^{(n-1)/2} & \text{if } n\text{ is odd}\end{cases}$$

The script implements the exponentiation in a bottom-up fashion,to avoid the overhead of the recursive calls. When computing large power module $M$, property $4.$ of **Proposition 8** allows us to deal only with the residues of multiplication.

## Combinatorics

### Permutations

**Definition 4:** A permutation of a set $S$ is an ordered arrangement of the elements of $S$.

The number of permutations of a set $S$ with $n$ different elements is denoted by $n!$, and is defined as $n!=n\cdot(n-1)\cdot...\cdot2\cdot1$. If our set $S$ reapeated elements, let's say $n_1$ elements of type $1$, $n_2$ elements of type $2$, and so on, then the number of indistinguishable permutations of $S$ is given by:

$$\dfrac{n!}{n_1!\cdot n_2!\cdot...\cdot n_k!}$$

To see this, let $x$ be the number of indistinguishable permutations of $S$. For each distinguishable permutation, there are $\prod_{i=1}^kn_i!$ indistinguishable permutations. So we have that $n!=x\prod_{i=1}^kn_i!$, and the result follows.

Another way of conceiving a permutation is through the concept of a bijection.

**Definition 5:** Let $E(n)$ an enumeration of $n$ objects. A permutation of $n$ elements is a bijection $\pi:E(n)\rightarrow E(n)$.

For example:

$$ \pi = \begin{pmatrix} e_1 & e_2 & e_3 & e_4 & e_5 \\ e_3 & e_5 & e_1 & e_4 & e_2 \end{pmatrix} $$

So here $\pi(e_1)=e_3$, $\pi(e_2)=e_5$. An interesting characteristic about permutation is the _desorder_. In the example we saw that $\pi(e_4)=e_4$, so $e_4$ is in order, while $e_1$ is out of order. When a permutation has no elements in order, we say that it is a _total disorder_. The number of total desorder for $n$ elements will be denoted by $D_n$. Next we enumerate some properties about $D_n$:

**Proposition 11:** Let $n\in\mathbb{N}$. Then:

1. Set $D(0)=1$. Then $D_n=(n-1)(D(n-1)+D(n-2))$.
2. $D_n=nD(n-1)+(-1)^n$.

The last proposition lead to te following awesome result:

**Theorem 7 (Total Desorder Formula):** Let $n\in\mathbb{N}$. Then we have:

$$ D_n = n!\sum_{i=0}^{n}\dfrac{(-1)^i}{i!} $$

**Example 1:** In a party, $n$ men throw their watches into a box. At the end of the party each man picks a watch at random from the box. In how many ways can the watches be distributed so that no man gets his own watch?

**Solution :** Since no man can get his own watch, if we tag each watch to its owner, then we have a total disorder. So the solution is $D_n$.

For a permutation of a collectio of $n$ elements, each permutation has from $0$ to $n$ disorders. So we can think of computing $n!$based on the number of permutations with $k$ disorders as follows:

**Theorem 8:**

$$ n! = \sum_{k=0}^{n}\binom{n}{k}D_k $$

### Binomial Coefficients

**Definition 6:** The binomial coefficient $\binom{n}{k}$ is the number of ways to choose $k$ elements from a set of $n$ elements. The binomial coefficient is defined as:

$$\binom{n}{k}=\dfrac{n!}{k!(n-k)!}$$

**Proposition 12:** Useful iterpretations of $\binom{n}{k}$:

1. The number of ways to choose $k$ elements from a set of $n$ elements.
2. The number of ways of dividing a set of $n$ elements into two sets of $k$ and $n-k$ elements.
3. The number of distributions of $k$ indistinguishable objects into $n$ distinguishable boxes where each box must contain at least one object.

**Proposition 13:** Let $n,k\in\mathbb{N}$. Then:

1. $\binom{n}{k}=\binom{n}{n-k}$.

2. $\binom{n}{k}=\binom{n-1}{k}+\binom{n-1}{k-1}$.

3. $\binom{n + m}{r}= \sum_{k=0}^{r}\binom{n}{k}\binom{m}{r-k}$.

4. $k\binom{n}{k}=n\binom{n-1}{k-1}$.

5. $(x+y)^n=\sum_{k=0}^{n}\binom{n}{k}x^{n-k}y^k$.

If for a set of n elements we want to know the number of ways to divide it into $m$ different groups of size $k_1,k_2,...,k_m$, $m\ge 2$, then the number of ways is given by:

$$\dfrac{n!}{k_1!k_2!...k_m!}$$

with the condition that $k_1+k_2+...+k_m=n$.

### Trayectory Counting

**Definition 7:** Let consider a particle that moves in a grid from the origin $(0,0)$ to the point $(m,n)$, with $m,n\in\mathbb{N}$. The particle can only move to the right or up. A trajectory is a sequence of moves that the particle makes to reach the point $(m,n)$.

Denoting $U$ for up and $R$ for right, a trajectory can be represented as a string of $m$ $R$'s and $n$ $U$'s. The number of trajectories is given by the number distinguishable permutations of the string. So the number of trajectories is given by $\binom{m+n}{m}$.

**Proposition 14:** Let $m,n\in\mathbb{N}$. Then the number of trajectories from $(0,0)$ to $(m,n)$ is given by $\binom{m+n}{m}$.

**Definition 8:(Dyck trayectory)** A Dyck trayectory is a trayectory from $(0,0)$ to $(n,n)$ that never goes below the diagonal $y=x$.

**Theorem 9:** The number of Dyck trayectories of length $2n$ is given by the $n$-th Catalan number, $C_n$ defined as:

$$C_n=\dfrac{1}{n+1}\binom{2n}{n}$$

**Example 2:** Let be $\{ x_i \}_{i=1}^{n}$ a sequence of $n$ elements where $x_i\in\{-1,1\}$. How many sequences are there such that $\sum_{i=1}^{n}x_i\ge 0$ ?

**Solution:** We can think of the problem as a particle that moves in a grid from $(0,0)$ to $(n,n)$, with $x_i=1$ representing a move to the right and $x_i=-1$ a move up. The condition $\sum_{i=1}^{n}x_i\ge 0$ is equivalent to the particle performing a Dyck trayectory. So the solution is $C_n$.

### Combinations with Repetition

We can ask the following: How many ways are there to distribute $n$ identical objects into $k$ distinguishable boxes? or How many ways are there to choose $n$ objects from a box with an infinite number of $k$ different objects?

It turns out that those questions are equivalent(why?) to the number of non-negative integer solutions to the equation $x_1+x_2+...+x_k=n$. To find out the number of solutions we can use trayectory counting. We can think of the problem as a particle that moves in a grid from $(0,0)$ to $(k,n+1)$, with $x_i$ representing the number of vertical steps in the $i$-th column. This way, each trayectory is univoquely associated with a solution to the equation. That leads to the following result:

**Theorem 10:** The number of non-negative integer solutions to the equation $x_1+x_2+...+x_k=n$ is given by $\binom{n+k-1}{n}$.

For the case when $x_i\ge 1$, if we set $y_i=x_i-1$, then we have the equation $y_1+y_2+...+y_k=n-k$. So the number of solutions is given by $\binom{n-1}{n-k}$.
