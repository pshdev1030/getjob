# Selector

## CSS rule

CSS rule은 다음을 포함한 한 블럭의 코드이다

- 하나 혹은 여러개의 선택자
- 선언

```css
/* 선택자 .my-css-rule*/
.my-css-rule {
  /* 선언 property:value*/
  background: red;
  color: beige;
  font-size: 1.2rem;
}
```

## Simple selectors

가장 간단한 선택자는 HTML요소와 클래스, id와 속성을 대상으로 한다.
특수문자 혹은 문자 집합을 사용한다.

### Universal selector

모든 element를 선택한다.
아래 코드는 모든 element의 글자색이 hotpink가 된다.

```css
* {
  color: hotpink;
}
```

### Type selector

HTML 요소에 직접 매칭된다.
아래 코드는 모든 section이 2em의 padding을 갖게된다.

```css
section {
  padding: 2em;
}
```

### Class selector

클래스 속성이 매칭되는 요소들을 선택한다
`.`문자는 클래스의 특정 멤버를 매칭하도록 지시하는 패턴이다.
아래 코드는 클래스명에 my-class를 포함하는 모든요소들의 글자색이 red가 된다.

```HTML
<div class="my-class"></div>
<button class="my-class"></button>
<p class="my-class"></p>
<div class="my-class another-class some-other-class"></div>
```

```css
.my-class {
  color: red;
}
```

### ID selector

id는 고유한 값으로 하나의 html에 같은 값이 존재할 수 없다.
`#`문자는 id를 지닌 멤버를 매칭시키는 패턴이다.
아래 코드는 id값으로 rad를 가지는 고유한 요소에 border를 만든다.

```HTML
<div id="rad"></div>
```

```css
#rad {
  border: 1px solid blue;
}
```

### Attribute selector

속성 선택자를 사용하여 특정 HTML 속성을 가졌거나 속성에 대한 특정값을 가진 요소들을 선택할 수 있다.
`[]`로 래핑하여 사용한다.

아래의 코드는 data-type값이 primary인 요소를 선택하여 글자색을 red로 만든다.

```html
<div data-type="primary"></div>
```

```css
[data-type="primary"] {
  color: red;
}
```

아래와 같이 작성하면 data-type속성의 value와 상관없이 data-type속성을 지닌 모든 요소를 선택한다.
아래의 코드는 두 div 모두 글자색이 red가 된다.

```html
<div data-type="primary"></div>
<div data-type="secondary"></div>
```

```css
[data-type] {
  color: red;
}
```

아래와 같이 작성하면 대소문자를 구분하여 선택한다.
Primary의 경우 적용되지 않습니다.

```css
[data-type="primary" s] {
  color: red;
}
```

이 외에도 다음과 같은 여러 속성들이 있다.

```css
/* A href that contains "example.com" */
[href*="example.com"] {
  color: red;
}

/* A href that starts with https */
[href^="https"] {
  color: green;
}

/* A href that ends with .com */
[href$=".com"] {
  color: blue;
}
```

## Grouping selectors

여러 선택자를 ','로 구분하여 선택할 수 있다.

```css
strong,
em,
.my-class,
[lang] {
  color: red;
}
```

## Pseudo-classes and pseudo-elements

css는 hover나 자식등 특정 상태에 초점을 맞춘 선택자도 제공한다

### Pseudo-classes

상태에 초점을 맞춘 선택자이다.
`:`를 사용한다.

#### :hover

아래 마우스 포인터가 올라왔을 때의 css를 작성할 수 있다.

```css
a:hover {
  outline: 1px dotted green;
}
```

#### :nth-child()

자식을 선택할 수 있다.

```css
p:nth-child(even) {
  background: floralwhite;
}
/* 짝수 */

p:nth-child(odd) {
  background: floralwhite;
}
/* 홀수 */
```

### Pseudo-element

요소의 앞이나 뒤에 새로운 요소를 삽입한다
`::`를 사용한다.

아래 코드는 요소의 앞에 새로운 content를 삽입한다.

```css
.my-element::before {
  content: "Prefix - ";
}
```

아래 코드는 리스트의 점 색을 바꾼다.

```css
li::marker {
  color: red;
}
```

아래 코드는 사용자에 의해서 선택될 경우의 css를 지정한다

```css
::selection {
  background: black;
  color: white;
}
```

## Complex selectors

복잡한 css의 경우 css에 계단식으로 접근할 수 있다.

### Combinators

`>` 문자를 사용함으로서 하위 요소에 접근할 수 있다.

```css
p > strong {
  color: blue;
}
```

### Decendant combinator

하위 요소를 선택한다.

아래 코드의 경우 strong 중 p를 부모로 가진 요소를 선택한다.

```css
p strong {
  color: blue;
}
```

### Next sibling combinator

`+` 키워드를 사용한다. 바로 옆의 요소들을 선택한다.

### Subsequent -sibling combinator

`~` 키워드를 사용한다. 같은 부모를 가진 다른 요소들을 선택한다.

### Compound selectors

선택자는 결합할 수 있다.

아래 코드는 my-class 클래스를 가진 a 요소를 선택한다

```css
a.my-class {
  color: red;
}
```
