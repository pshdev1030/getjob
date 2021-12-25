# The cascade

여러 css 규칙이 html 요소에 적용되었을 때 이 충돌을 해결하기 위한 알고리즘이다.

## Cascade algorithm

1. 위치 및 표시 순서

- css 규칙이 나타나는 순서

2. 특수성

- 가장 강력하게 매치되는 css 선택자 결정 알고리즘

3. 출처

- css 가 나타나는 시점과 출처, 브라우저 스타일, 브라우저 확장자, 또는 사용자가 작성한 css 순서

4. 중요도

- 몇몇 css는 다른 css보다 더 많은 중요도를 가진다.
  특히 `!import`가 적용된 css들은 중요도가 더 높다.

## 위치 및 표시 순서

- cascade algorithm에 따라 css 규칙의 순서가 계산된다.

구체적일수록 또 아래에 선언될수록 해당 css가 선택된다.

예를들어 인라인 style의 경우 important속성이 없는 한 우선적으로 적용된다.

또한 브라우저는 이해하지 못하는 값을 무시하기 때문에 특정 값을 지원하지 않는 브라우저를 위해
두 가지 속성을 정의하는 것은 의미있다.

아래의 코드는 clamp를 지원하지 않는 브라우저는 1.5rem의 font-size를 갖게된다.

```css
.my-element {
  font-size: 1.5rem;
  font-size: clamp(1.5rem, calc(1rem + 3vw), 2rem);
}
```

## 특수성

가중치 시스템을 통해 어떤 css가 구체적인지 결정하는 알고리즘이다.

요소를 대상으로 하는 css보다 클래스를 대상으로 하는 css가 구체적인 css로 간주된다.

## 출처

css는 출처에 따라 구체적인지 구체적인지 아닌지도 결정한다

가장 구체적이지 않은 css부터 가장 구체적인 css 순으로 정렬하자면

1. 브라우저 기본 스타일
   HTML 요소에 기본적으로 적용되는 스타일이다.

2. 로컬 사용자 스타일
   기본 글꼴과 같은 os단에서 적용하는 스타일이다.

3. 직접 작성한 css
   사용자가 직접 작성한 css

4. 직접 작성한 !important가 포함된 css
   !important 속성이 추가된 css

5. 로컬 사용자 !important 스타일
   !important가 추가된 os단에서 적용하는 스타일이다.

6. 브라우저 !important 스타일
   브라우저에서 제공하는 !import속성이 있는 css이다.

## 중요도

css 규칙마다의 중요도도 존재한다
가장 중요하지 않은 css부터 가장 중요한 css순으로 정렬하자면

1. 일반 규칙

2. animation

3. !important 규칙

4. transition 규칙
