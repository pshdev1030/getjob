# 박스모델

아래 코드의 결과는 100px가 아닌 142px가 된다. 또한 텍스트는 박스를 벗어나게 된다.

```HTML
<p>I am a paragraph of text that has a few words in it.</p>
```

```css
p {
  width: 100px;
  height: 50px;
  padding: 20px;
  border: 1px solid;
}
```

## 컨텐츠와 사이즈

박스는 박스마다 동작하는 방식이 다르다.
이는 아래 요인의 영향을 받는다.

1. display
2. set dimension
3. content

컨텐츠에 따라 width값을 조절하는 것이 유연하다.

### min-content

담고있는 content에 의해 width 속성값을 결정한다.
박스에 content의 본질적인 최소 너비만큼의 width를 가지도록 지시한다.
텍스트의 경우 최대한 줄바꿈을 하고 가장 긴 단어의 길이가 최소 너비가 된다.
오버플로우가 발생하지 않는다.

```css
p {
  width: min-content;
}
```

### max-content

담고있는 content에 의해 width 속성값을 결정한다.
박스에 content의 본질적인 최대 너비만큼의 width를 가지도록 지시한다.
텍스트의 경우 줄바꿈을 하지 않은 상태의 문장의 길이가 최대 너비가 된다.
오버플로우가 발생할 수 있다.

```css
p {
  width: max-content;
}
```

### fit-content

width가 컨텐츠를 담기에 부족하지 않은 경우에는 `max-content`를 사용한다.
하지만 부족해질 경우 auto처럼 여백을 제외한 너비를 엘리먼트의 width값으로 사용한다.

## Box Model

<img src="https://web-dev.imgix.net/image/VbAJIREinuYvovrBzzvEyZOpw5w1/ECuEOJEGnudhXW5JEFih.svg" alt="box">

1. content box
   content가 존재하는 영역으로 가변적인 영역이다

2. padding box
   content box를 둘러싸고 있으며 박스 안에 존재한다.
   상자의 배경은 padding box에도 적용된다.
   또한 overflow 규칙 또한 padding을 포함하여 적용된다.

3. border box
   padding box를 둘러싸고 있다. 액자의 틀이라고 생각하면 된다.

4. margin box
   box의 크기에 영향을 주지않는 영역이다.
   box 밖의 여백으로 생각할 수 있다.
   outline-width속성은 이 margin-box값까지 포함한 값을 나타낸다.

## Controlling the box model

### basic css

모든 브라우저는 HTMl문서에 기본적인 css를 적용한다.
이는 모든 종류의 box에 display또한 정의되어있음을 의미한다.

1. block
   사용 가능한 인라인 영역을 채운다.
   높이값을 지정할 수 있다.

2. inline
   글자와 같다고 생각하면 된다.
   내용물만큼 커진다.
   블록 마진을 가지고 있지만 고려되지 않는다.

3. inline block
   inline과 같이 동작하지만 높이값을 가질 수 있다.

### box-sizing

상자 크기를 계산하는 방법을 제어하는 속성이다.

1. box-sizing:content-box
   브라우저가 제공하는 기본값이다.
   padding 과 border에 영향을 받는다.
   즉 실제 width=width+padding+border이다.
   아래의 경우 200+10*2+20*2로 실제 width는 260이다.

   ```css
   p {
     width: 200px;
     padding: 20px;
     border: 10px solid;
   }
   ```

2. border-box
   `box-sizing:border-box;`로 설정할 수 있다.
   padding 과 border을 포함한 값이 width가 된다.

   즉 실제 width=width이다.
   아래의 경우 width값 200안에 10*2(border)와 20*2(padding)을 모두 포함한다.
   때문에 실제 width는 200이다.

   ```css
   p {
     box-sizing: border-box;
     width: 200px;
     padding: 20px;
     border: 10px solid;
   }
   ```

### 문서의 모든 요소 선택하기

문서의 모든 요소가 계산한 대로 동작하도록 하는 css이다.

    ```css
    *,
    *::before,
    *::after {
    box-sizing: border-box;
    }
    ```

## ref

https://www.daleseo.com/css-width/
https://web.dev/learn/css/box-model/
