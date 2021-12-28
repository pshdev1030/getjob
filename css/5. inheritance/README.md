# inheritance

css속성에는 상속이 발생한다.

## inheritance flow

상위요소에서 하위 요소로 계단식으로 상속된다.

다음 html에 css를 적용하면 글자색이 변경된다.

```html
<html>
  <body>
    <article>
      <p>Lorem ipsum dolor sit amet.</p>
    </article>
  </body>
</html>
```

```css
html {
  color: lightslategray;
}
```

## How to explicitly inherit and control inheritance

css에서 제공하는 키워드를 통해 명시적으로 상속을 컨트롤 할 수 있다.

`all` 속성을 사용하여 한 번에 적용할 수 있다.

### inherit

`inherit` 키워드를 사용하여 부모의 값을 사용하도록 할 수 있다.

```css
strong {
  font-weight: 900;
}
```

### innitial

`initial` 키워드를 사용하여 기본값을 사용하도록 할 수 있다.

```css
aside strong {
  font-weight: initial;
}
```

### unset

상속할 값이 존재하면 상속값을 그렇지 않으면 초깃값을 사용한다.
즉 상속이 있을경우 `inherit` 없을 경우 `initial`로 동작한다.

```css
/* Global color styles for paragraph in authored CSS */
p {
  margin-top: 2em;
  color: goldenrod;
}

/* The p needs to be reset in asides, so you can use unset */
aside p {
  margin: unset;
  color: unset;
}
```
