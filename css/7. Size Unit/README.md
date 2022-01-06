## Size Unit

명시적으로 사이즈를 지정하는 css에는 여러가지가 있다.

## Number

숫자는 여러 css에 사용된다.
문맥에 따라 비율 혹은 명시적인 크기의 의미를 가진다.
`line-height`에서 단위없이 숫자를 정의하는 경우 비율의 의미를 가진다.(150%와 동일하다)

```css
font-size: 24px;
line-height: 1.5;
```

## Percentages

css에선 상위 요소를 기준으로 하여 백분율로 계산된다.

```css
div {
  width: 300px;
  height: 100px;
}

div p {
  margin-top: 50%; /* calculated: 150px */
  padding-left: 50%; /* calculated: 150px */
}
```

## Demensions and length

### Absolute length

절대길이는 어떠한 맥락에서든 고정된 값을 가져서 사용되는 모든 위치에서 실제 size가 예측 가능하다.

```css
div {
  width: 10cm;
  height: 5cm;
  background: black;
}
```

| Unit | Name                | Equivalent to       |
| ---- | ------------------- | ------------------- |
| cm   | Centimeters         | 1cm = 96px/2.54     |
| mm   | Millimeters         | 1mm = 1/10th of 1cm |
| Q    | Quarter-millimeters | 1Q = 1/40th of 1cm  |
| in   | Inches              | 1in = 2.54cm = 96px |
| pc   | Picas               | 1pc = 1/6th of 1in  |
| pt   | Points              | 1pt = 1/72th of 1in |
| px   | Pixels              | 1px = 1/96th of 1in |

### Relative length

상대길이는 백분율과 거의 같은 기준값에 의해 계산된다.
상대길이는 반응형 웹을 작성하는데에 유용하다.

#### Font-size-relative units

| unit | relative to:                                                                                |
| ---- | ------------------------------------------------------------------------------------------- |
| em   | 1em은 부모의 기본 글꼴 크기를 가진다.                                                       |
| ex   | x문자의 높이를 나타낸다. x문자를 가진 글꼴에서는 보통 소문자 높이와 같다. 1ex ≈ 0.5em 이다. |
| cap  | 영문 대문자의 평균 높이값을 나타낸다.(cap height)                                           |
| ch   | 문자 0의 너비이다. 너비0.5에 높이 1em이라고 가정한다.                                       |
| ic   | "水" 을 렌더링 할 때 사용하는 글꼴에서의 너비이다.                                          |
| rem  | em과 계산방식이 동일하며 최상위 태그를 기준으로 한다.(default is 16px).                     |
| lh   | 요소의 높이 값                                                                              |
| rlh  | 최상위 태그의 높이값                                                                        |

## Viewport - relative units

| unit | relative to                              |
| ---- | ---------------------------------------- |
| vw   | 1vw의 경우 뷰포트 너비의 1%값을 가진다.  |
| vh   | 1 vh의 경우 뷰포트 높이의 1%값을 가진다. |
| vmin | 뷰포트의 너비와 높이중 더 작은 값        |
| vmax | 뷰포트의 너비와 높이중 더 큰 값          |

## Miscellaneous units

### Angle units

각도를 계산하는 단위이다.

```css
div {
  width: 150px;
  height: 150px;
  transform: rotate(60deg);
}
```
