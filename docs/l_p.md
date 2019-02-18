# $L_p$-norms and $L_p$-metrics

## Norms

In the simple case of a finite-dimensional vector stapce $V$, the $L_p$ norm (often just denoted $\ell_p$) is defined for $v = (v_1,\ldots,v_n) \in V$ to be
\[
  {\|v\|}_p := \left(\sum_{i=1}^n v_i^p\right)^{\frac{1}{p}}
\]
The most popular such norm is the $L_2$ norm (i.e. the Euclidean norm) for which we can see the Pythagorean theorem generalized.
\[
  {\|(a,b)\|}_2 = \sqrt{a^2 + b^2}
\]
The $L_2$ norm is special in that it can also be expressed in terms of an inner product.
That is ${\|v\|}_2 = v^\top v$.

Other popular choices for $p$ include $p=1$ and $p= \infty$.

\[
  {\|v\|}_1 := \sum_{i=1}^n v_i
\]

\[
  {\|v\|}_\infty := \max_{i\in \{1,\ldots, n\}} v_i
\]
For a trajectory $f:[0,1] \to \mathbb{R}^d$, one can also define a norm.
The simplest of these would be
\[
  {\|f\|}_1 := \int_0^1 {\|f(t)\|}_2 dt
\]
Don't be surprised that we are hiding the $L_2$ norm on the points inside the $L_1$ norm on trajectories.
We will do the same for other norms.

\[
  {\|f\|}_2 := \left(\int_0^1 {\|f(t)\|}_2^2 dt\right)^{\frac{1}{2}}
\]

\[
  {\|f\|}_\infty := \max_{t\in [0,1]} {\|f(t)\|}_2
\]

The $L_2$ norm on trajectories also has an inner product formulation.

\[
  {\|f\|}_2 := \left(\int_0^1 f(t)^\top f(t) dt\right)^{\frac{1}{2}}
  = \sqrt{f^\top f}
\]

## From norms to metrics

Once you understand trajectories as vectors in a (normed) vector space, it is easy to turn a norm into a metric.
The $L_p$ distance between trajectories $f$ and $g$ is ${\|f-g\|}_p$.


## Evaluating the $L_2$ distance on piecewise linear trajectories.

Let's work out the $L_2$ distance between two line segments.
Let $u,v,x,y$ be points in $\mathbb{R}^d$.
Let $f$ and $g$ be the line segments $\overline{uv}$ and $\overline{xy}$ respectively.
That is, $f(t) = (1-t)u + t(v)$ and $g(t) = (1-t)x + ty$.

Our goal is to compute ${\|f-g\|}_2$.
It helps to first observe that $(f-g)(t) = (1-t)(u-x) + t(v - y)$.
Thus, the difference is also a line segment.
Let $a=u-x$ and $b = v-y$.
Then,
\[
{\|f-g\|}_2 = \int_0^1 {\|(1-t)a + tb\|}_2^2 dt
\]
Expanding the squared term in the middle gives the following.

\[
{\|f-g\|}_2 =
\left({\|a\|}_2^2 \int_0^1 (1-t)^2 dt\right)
+
\left(2a^\top b \int_0^1 t(1-t)dt\right)
+
\left({\|b\|}_2^2 \int_0^1 t^2 dt\right)
\]
\[
= \frac{1}{3}\left({\|a\|}_2^2
+
a^\top b
+
{\|b\|}_2^2\right)
\]
