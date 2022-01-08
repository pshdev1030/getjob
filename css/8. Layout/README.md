## Layout

CSS는 수평축, 수직축에서 배치를 위한 다양한 방법을 제공한다.

## Layout: the present and future

현재 Flexbox와 Grid와 같은 좋은 도구들이 있다.

## display

box가 `inline`으로 작동할지 `block`으로 작동할지 결정한다.

### inline

`inline`은 문장에서 단어처럼 배치된다.
명시적인 너비와 높이를 설정할 수 없다.
또한 `margin`과 `padding` 또한 무시된다.
ex) `<span>`,`<p>`

### block

`block` 요소는 다른 요소와 나란히 배치되지 않고 새로운 선을 만든다.
`inline` dimension에서 최대의 크기를 가진다.

또한 `margin`과 `padding`을 가질 수 있다.

```css
.my-element {
  display: block;
}
```

## flexbox

1차원 배치를 위한 배치 매커니즘이다.
단일 축을 기준으로 배치할 수 있다.

```css
.my-element {
  display: flex;
}
```

## grid

다중 축 레이아웃을 제어하기 위해 설계된 매커니즘이다.
하나의 격자를 fr단위로 제어할 수 있다.

```css
.my-element {
  display: grid;
}
```

## float

주변 요소를 정렬하는 규칙을 정한다.

```css
img {
  float: left;
  margin-right: 1em;
}
```

## Multicolumn layout

여러 열로 분할하는 규칙이다.

```css
.countries {
  column-count: 2;
  column-gap: 1em;
}
```

## position

요소가 어떻게 동작하는지, 다른 요소와 어떻게 관련되는지를 변경한다.

```css
.my-element {
  position: relative;
  top: 10px;
}
```
