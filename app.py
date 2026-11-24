<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>형량 예측 - 교육용 법률 참고 앱</title>
  <!-- Tailwind CSS 로드 -->
  <script src="https://cdn.tailwindcss.com"></script>
  <!-- Google Fonts (Noto Sans KR & Inter) -->
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;800&family=Noto+Sans+KR:wght@400;500;700;800&display=swap" rel="stylesheet" />
  <style>
    body {
      font-family: 'Noto Sans KR', 'Inter', sans-serif;
    }
    /* 커스텀 슬라이더 스타일 */
    input[type="range"] {
      -webkit-appearance: none;
      appearance: none;
      background: transparent;
      cursor: pointer;
    }
    input[type="range"]::-webkit-slider-runnable-track {
      height: 0.5rem;
      border-radius: 9999px;
      background: #e2e8f0;
    }
    input[type="range"]::-webkit-slider-thumb {
      -webkit-appearance: none;
      appearance: none;
      margin-top: -6px;
      background-color: #2563eb;
      height: 1.25rem;
      width: 1.25rem;
      border-radius: 9999px;
      border: 3px solid #ffffff;
      box-shadow: 0 2px 6px rgba(37, 99, 235, 0.4);
      transition: transform 0.15s ease;
    }
    input[type="range"]::-webkit-slider-thumb:hover {
      transform: scale(1.15);
    }
  </style>
</head>
<body class="bg-slate-100 text-slate-800 min-h-screen flex flex-col justify-between antialiased selection:bg-blue-100 selection:text-blue-900">

  <!-- 상단 교육용 안내 배너 -->
  <header class="bg-amber-50 border-b border-amber-200 px-4 py-2.5 text-center">
    <p class="text-xs sm:text-sm text-amber-900 font-medium flex items-center justify-center gap-1.5">
      <svg class="w-4 h-4 text-amber-600 shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24">
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
      </svg>
      <span>본 앱은 수업 및 조례·법률 학습을 위한 <strong>단순 참고용 시뮬레이터</strong>이며, 실제 사법부의 판결 기준과 다를 수 있습니다.</span>
    </p>
  </header>

  <!-- 메인 컨테이너 -->
  <main class="w-full max-w-xl mx-auto px-4 py-8 sm:py-12 flex-1">
    <div class="bg-white rounded-3xl shadow-xl shadow-slate-200/70 border border-slate-200/80 overflow-hidden">
      
      <!-- 앱 타이틀 헤더 -->
      <div class="bg-gradient-to-r from-slate-900 via-slate-800 to-blue-950 px-6 py-7 text-white">
        <div class="inline-flex items-center gap-1.5 px-3 py-1 rounded-full bg-blue-500/20 border border-blue-400/30 text-blue-200 text-xs font-semibold mb-3">
          <span>⚖️ 법률 기초 학습 도구</span>
        </div>
        <h1 class="text-2xl sm:text-3xl font-extrabold tracking-tight">형량 예측</h1>
        <p class="text-slate-300 text-sm mt-1.5">범죄 유형과 나이를 선택하여 참고 형량 및 촉법소년 여부를 확인해 보세요.</p>
      </div>

      <!-- 입력 영역 -->
      <div class="p-6 sm:p-8 space-y-7">
        
        <!-- 1. 범죄 종류 선택 -->
        <div>
          <label class="block text-sm font-bold text-slate-700 mb-3">
            1. 범죄 종류 선택
          </label>
          <div id="crime-options" class="grid grid-cols-2 sm:grid-cols-4 gap-2.5">
            <!-- 살인 -->
            <label class="cursor-pointer">
              <input type="radio" name="crimeChoice" value="살인" class="peer sr-only" checked />
              <div class="p-3 rounded-2xl border-2 border-slate-200 bg-slate-50/50 text-center font-bold text-slate-700 transition-all peer-checked:border-blue-600 peer-checked:bg-blue-50 peer-checked:text-blue-700 hover:bg-slate-100">
                살인
              </div>
            </label>
            <!-- 마약 -->
            <label class="cursor-pointer">
              <input type="radio" name="crimeChoice" value="마약" class="peer sr-only" />
              <div class="p-3 rounded-2xl border-2 border-slate-200 bg-slate-50/50 text-center font-bold text-slate-700 transition-all peer-checked:border-blue-600 peer-checked:bg-blue-50 peer-checked:text-blue-700 hover:bg-slate-100">
                마약
              </div>
            </label>
            <!-- 절도 -->
            <label class="cursor-pointer">
              <input type="radio" name="crimeChoice" value="절도" class="peer sr-only" />
              <div class="p-3 rounded-2xl border-2 border-slate-200 bg-slate-50/50 text-center font-bold text-slate-700 transition-all peer-checked:border-blue-600 peer-checked:bg-blue-50 peer-checked:text-blue-700 hover:bg-slate-100">
                절도
              </div>
            </label>
            <!-- 폭행 -->
            <label class="cursor-pointer">
              <input type="radio" name="crimeChoice" value="폭행" class="peer sr-only" />
              <div class="p-3 rounded-2xl border-2 border-slate-200 bg-slate-50/50 text-center font-bold text-slate-700 transition-all peer-checked:border-blue-600 peer-checked:bg-blue-50 peer-checked:text-blue-700 hover:bg-slate-100">
                폭행
              </div>
            </label>
          </div>
        </div>

        <!-- 2. 나이 입력 (슬라이더: 5~100) -->
        <div>
          <div class="flex items-center justify-between mb-2">
            <label for="age-slider" class="text-sm font-bold text-slate-700">
              2. 나이 입력
            </label>
            <div class="flex items-center gap-2">
              <span id="age-badge-hint" class="text-xs font-semibold px-2.5 py-0.5 rounded-full bg-slate-100 text-slate-600">
                만 14세 이상
              </span>
              <span class="text-lg font-extrabold text-blue-600 tabular-nums">
                <span id="age-display">20</span>세
              </span>
            </div>
          </div>

          <div class="bg-slate-50 border border-slate-200/80 rounded-2xl p-4">
            <input
              id="age-slider"
              type="range"
              min="5"
              max="100"
              value="20"
              class="w-full"
              aria-label="나이 선택 슬라이더"
            />
            <div class="flex justify-between text-xs text-slate-400 font-medium mt-2 px-0.5">
              <span>5세</span>
              <span class="text-amber-600 font-semibold">14세 (촉법 기준)</span>
              <span>50세</span>
              <span>100세</span>
            </div>
          </div>
        </div>

        <!-- 분석하기 버튼 -->
        <button
          id="analyze-btn"
          type="button"
          onclick="checkRisk()"
          class="w-full py-3.5 px-6 rounded-2xl bg-blue-600 hover:bg-blue-700 active:scale-[0.99] text-white font-bold text-base shadow-lg shadow-blue-600/25 transition-all flex items-center justify-center gap-2 cursor-pointer"
        >
          <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2m-6 9l2 2 4-4" />
          </svg>
          <span>분석하기</span>
        </button>

        <!-- 구분선 -->
        <hr class="border-slate-200" />

        <!-- 결과 출력 화면 -->
        <section aria-live="polite" class="space-y-4">
          <div class="flex items-center justify-between">
            <h2 class="text-sm font-bold text-slate-500 uppercase tracking-wider">결과 출력 화면</h2>
            <span id="result-timestamp" class="text-xs text-slate-400"></span>
          </div>

          <div id="result-box" class="rounded-2xl border-2 border-slate-200 bg-slate-50 p-5 sm:p-6 transition-all">
            <!-- 초기 안내 문구 -->
            <div id="result-placeholder" class="text-center py-4 text-slate-400 text-sm">
              범죄 종류와 나이를 선택한 후 <strong>[분석하기]</strong> 버튼을 눌러주세요.
            </div>

            <!-- 실제 분석 결과 영역 -->
            <div id="result-content" class="hidden space-y-4">
              <!-- 1) 촉법 여부 텍스트 메시지 -->
              <div class="flex items-start gap-2.5">
                <span class="text-slate-400 font-bold select-none">-</span>
                <div>
                  <span id="juvenile-status" class="inline-block px-3 py-1 rounded-lg text-sm font-extrabold">
                    촉법이 아님
                  </span>
                  <p id="juvenile-desc" class="text-xs text-slate-500 mt-1"></p>
                </div>
              </div>

              <!-- 2) for 반복문을 통해 배치된 형량 출력 영역 -->
              <div id="sentence-list-container" class="space-y-2">
                <!-- JavaScript의 for 구문으로 동적 생성됨 -->
              </div>

              <!-- 3) 착하게 삽시다 (두꺼운 글자로 표시) -->
              <div class="pt-3 border-t border-slate-200/80 flex items-center gap-2">
                <span class="text-slate-400 font-bold select-none">-</span>
                <p class="text-lg sm:text-xl font-extrabold text-slate-900 tracking-tight">
                  <strong>착하게 삽시다</strong>
                </p>
              </div>
            </div>
          </div>
        </section>

        <!-- 학습용 핵심 알고리즘 코드 보기 토글 -->
        <div class="pt-2">
          <button
            type="button"
            onclick="toggleCodePreview()"
            class="w-full py-2.5 px-4 rounded-xl bg-slate-100 hover:bg-slate-200/80 text-slate-600 text-xs font-bold transition-colors flex items-center justify-between cursor-pointer"
          >
            <span>💻 수업 학습용: 핵심 알고리즘 구조 보기 (리스트 · if · for)</span>
            <span id="code-toggle-icon">펼치기 ▼</span>
          </button>

          <div id="code-preview-panel" class="hidden mt-3 rounded-2xl bg-slate-900 text-slate-100 p-4 text-xs overflow-x-auto leading-relaxed font-mono">
<pre><code>// 1. 리스트 선언: 범죄 종류별 기본 형량 정의
const crimeList = [
  { name: "살인", minYears: 5, maxYears: 30 },
  { name: "마약", minYears: 1, maxYears: 10 },
  { name: "절도", minYears: 1, maxYears: 6 },
  { name: "폭행", minYears: 1, maxYears: 5 }
];

function checkRisk() {
  // 2. 입력받기: choice로 범죄 선택, age로 나이 입력
  let choice = selectedCrime;
  let age = Number(sliderValue);

  // 3. 조건판단 (if 구문): 14세 미만이면 촉법임 및 형량 -5 감점
  let deduction = 0;
  if (age &lt; 14) {
    statusMessage = "촉법임";
    deduction = 5;
  } else {
    statusMessage = "촉법이 아님";
  }

  // 4. 반복 출력 (for 구문): 리스트를 순회하며 선택된 범죄 형량 배치
  for (let i = 0; i &lt; crimeList.length; i++) {
    if (crimeList[i].name === choice) {
      let finalMin = Math.max(0, crimeList[i].minYears - deduction);
      let finalMax = Math.max(0, crimeList[i].maxYears - deduction);
      // 화면에 출력: `${choice}: ${finalMin}~${finalMax}년`
    }
  }
}</code></pre>
          </div>
        </div>

      </div>
    </div>
  </main>

  <!-- 하단 푸터 -->
  <footer class="text-center py-5 px-4 text-xs text-slate-400">
    교육 및 법률 이해 증진을 위해 제작된 참고용 프로그램입니다.
  </footer>

  <script>
    // ==========================================
    // 1. 리스트 선언: 범죄 종류별 기준 형량(단위: 년) 정의
    // ==========================================
    const crimeList = [
      { name: "살인", minYears: 5, maxYears: 30 },
      { name: "마약", minYears: 1, maxYears: 10 },
      { name: "절도", minYears: 1, maxYears: 6 },
      { name: "폭행", minYears: 1, maxYears: 5 }
    ];

    // 전역 입력 변수 선언 (choice: 범죄 선택, age: 나이 입력)
    let choice = "살인";
    let age = 20;

    // DOM 요소 참조
    const ageSlider = document.getElementById("age-slider");
    const ageDisplay = document.getElementById("age-display");
    const ageBadgeHint = document.getElementById("age-badge-hint");

    // 슬라이더 조작 시 실시간 나이(age) 업데이트
    ageSlider.addEventListener("input", function () {
      age = parseInt(this.value, 10);
      ageDisplay.textContent = age;

      if (age < 14) {
        ageBadgeHint.textContent = "만 14세 미만 (촉법 해당)";
        ageBadgeHint.className = "text-xs font-semibold px-2.5 py-0.5 rounded-full bg-amber-100 text-amber-800";
      } else {
        ageBadgeHint.textContent = "만 14세 이상";
        ageBadgeHint.className = "text-xs font-semibold px-2.5 py-0.5 rounded-full bg-slate-100 text-slate-600";
      }
    });

    // ==========================================
    // 2. 분석하기 버튼 클릭 시 실행되는 checkRisk() 함수
    // ==========================================
    function checkRisk() {
      // 라디오 버튼에서 선택된 범죄(choice)와 슬라이더의 나이(age) 가져오기
      const selectedRadio = document.querySelector('input[name="crimeChoice"]:checked');
      choice = selectedRadio ? selectedRadio.value : "살인";
      age = parseInt(ageSlider.value, 10);

      // UI 요소 참조
      const resultPlaceholder = document.getElementById("result-placeholder");
      const resultContent = document.getElementById("result-content");
      const resultBox = document.getElementById("result-box");
      const juvenileStatusEl = document.getElementById("juvenile-status");
      const juvenileDescEl = document.getElementById("juvenile-desc");
      const sentenceListContainer = document.getElementById("sentence-list-container");
      const resultTimestamp = document.getElementById("result-timestamp");

      // 결과 화면 활성화
      resultPlaceholder.classList.add("hidden");
      resultContent.classList.remove("hidden");

      // ==========================================
      // 3. 조건판단 (if 구문): 나이가 14세 미만이라면 촉법임 및 형량 -5 감점
      // ==========================================
      let isJuvenile = false;
      let deduction = 0;

      if (age < 14) {
        isJuvenile = true;
        deduction = 5; // 촉법이므로 형량 -5년 감경
        juvenileStatusEl.textContent = "촉법임";
        juvenileStatusEl.className = "inline-block px-3 py-1 rounded-lg text-sm font-extrabold bg-amber-100 text-amber-800 border border-amber-300";
        juvenileDescEl.textContent = `입력 나이(${age}세)는 만 14세 미만이므로 촉법소년에 해당하여 기본 형량에서 5년이 감경됩니다.`;
        resultBox.className = "rounded-2xl border-2 border-amber-300 bg-amber-50/40 p-5 sm:p-6 transition-all";
      } else {
        isJuvenile = false;
        deduction = 0;
        juvenileStatusEl.textContent = "촉법이 아님";
        juvenileStatusEl.className = "inline-block px-3 py-1 rounded-lg text-sm font-extrabold bg-blue-100 text-blue-800 border border-blue-200";
        juvenileDescEl.textContent = `입력 나이(${age}세)는 만 14세 이상으로 일반 형사 기준이 참고 적용됩니다.`;
        resultBox.className = "rounded-2xl border-2 border-blue-200 bg-blue-50/30 p-5 sm:p-6 transition-all";
      }

      // 기존 출력 초기화
      sentenceListContainer.innerHTML = "";

      // ==========================================
      // 4. 반복 출력 (for 구문): 리스트를 순회하며 선택된 범죄의 형량 배치
      // ==========================================
      for (let i = 0; i < crimeList.length; i++) {
        const currentCrime = crimeList[i];

        // 사용자가 선택한 범죄(choice)와 일치하는 항목을 화면에 배치
        if (currentCrime.name === choice) {
          // 감점 적용 시 최소 0년 미만으로 내려가지 않도록 처리
          const adjustedMin = Math.max(0, currentCrime.minYears - deduction);
          const adjustedMax = Math.max(0, currentCrime.maxYears - deduction);

          const row = document.createElement("div");
          row.className = "flex items-center gap-2.5 bg-white p-3.5 rounded-xl border border-slate-200 shadow-sm";

          const deductionTag = isJuvenile
            ? `<span class="ml-2 text-xs font-bold px-2 py-0.5 rounded-md bg-amber-100 text-amber-800">촉법 감경 -5년 적용</span>`
            : "";

          row.innerHTML = `
            <span class="text-slate-400 font-bold select-none">-</span>
            <div class="flex flex-wrap items-center">
              <span class="text-base sm:text-lg font-bold text-slate-900">
                ${currentCrime.name}: <span class="text-blue-600">${adjustedMin}~${adjustedMax}년</span>
              </span>
              ${deductionTag}
            </div>
          `;

          sentenceListContainer.appendChild(row);
        }
      }

      // 분석 시각 표시
      const now = new Date();
      resultTimestamp.textContent = `${now.getHours().toString().padStart(2, "0")}:${now.getMinutes().toString().padStart(2, "0")} 기준 참고 결과`;
    }

    // 학습용 코드 패널 열기/닫기 함수
    function toggleCodePreview() {
      const panel = document.getElementById("code-preview-panel");
      const icon = document.getElementById("code-toggle-icon");
      if (panel.classList.contains("hidden")) {
        panel.classList.remove("hidden");
        icon.textContent = "접기 ▲";
      } else {
        panel.classList.add("hidden");
        icon.textContent = "펼치기 ▼";
      }
    }
  </script>
</body>
</html>
