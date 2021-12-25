# 01

## style.css

### body

- min- height로 여백을 확보함

### section

- absolute값을 사용하기 위해 relative를 사용
- flex를 통해 이미지를 정렬해줌

### section:before

- absolute를 주고 bottom 0을 통해 최하단에 배치함
- background: linear-gradient 속성을 사용하여 이미지의 경계를 배경색과 같은 그라데이션으로 처리함

### section:after

- mix-blend 요소를 통해 필터를 정의해줌

### section img

- absolute 속성을 주고 같은 위치에서 시작하도록 정렬해줌
- object-fit을 통해 마찬가지로 section에 꽉채움

### text

- z index를 주어 상단에 위치하게함

### road

- z index를 text보다 높게 주어 text가 스크롤이 내려감에 따라 없어지게함

## main.js

scrollY값을 이용하여 요소들이 마우스의 스크롤 속도보다 느리게 움직이도록 수정한다.

## css

### linear-gradient

선형 그래디언트

linear-gradient(방향, 색)

### mix-blend-mode

자료형이 겹칠 경우 색상이 어떻게 나타나야 하는지 정의
최종 색상은 혼합모드를 적용한 픽셀 하나씩에 대해 전경색과 배경색을 취한 후 모드에 따라 계산을 수행하여 나온 새로운 값

- normal
  최상단 색을 사용

- multiply
  전경과 배경색을 곱한 값

- screen
  전경과 배경색을 반전한후 곱해 나온 값을 반전

- overlay
  배경색이 더 어두운 경우 multiply 더 밝은 경우 screen

- color
  전경색의 색조와 채도를 가지며 배경색의 밝기를 가진다.
  회색조를 유지하므로 전경을 색칠할 떄에 사용

- luminosity
  전경색의 밝기를 가지며 배경색의 색조와 채도를 가진다.

### pointer-event

요소가 어떤 경우에 이벤트의 대상이 되는지
