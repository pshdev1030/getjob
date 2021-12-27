# Specificity

중복된 css가 있을 때 점수를 계산하는 방식이다.
선택자에 따라 다른 가중치를 가진다.

## Univarsal selector

`*` 선택자는 0 포인트이다.
1 이상의 점수를 가지는 선택자가 오버라이딩된다.

```css
* {
  color: red;
}
```

## Element or pseudo-element selector

요소나 의사 dyth 선택자는 1포인트이다.

```css
div {
  color: red;
}

::selection {
  color: red;
}
```

## Class, pseudo-class, attribute selector

클래스, 의사클래스, 속성 선택자는 10포인트를 가진다.

```css
.my-class {
  color: red;
}

:hover {
  color: red;
}

[href="#"] {
  color: red;
}
```

### not 선택자

아래 코드의 경우 11point를 가진다
div+.my-class=11pt

```css
div:not(.my-class) {
  color: red;
}
```

## ID selector

ID 선택자는 1000point를 가진다.

```css
#myID {
  color: red;
}
```

## Inline Style attribute

인라인 스타일은 10000point를 가진다.

```html
<div style="color: red"></div>
```

## !important rule

!important 는 10000point를 가진다.

```css
.my-class {
  color: red !important; /* 10,000 points */
  background: white; /* 10 points */
}
```
