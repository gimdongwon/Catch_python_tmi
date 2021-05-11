function solution(new_id) {
  // 1.대문자를 소문자로
  new_id = new_id.toLowerCase();
  // 2. 소문자, 숫자, -, _, . 을 제외하고는 삭제
  new_id = new_id.replace(/[^0-9a-z-_.]/g, "");
  // 3. 마침표 중복 제거
  new_id = new_id.replace(/\.{2,}/g, ".");
  // 4. 마침표가 처음과 끝에 위치하면 삭제
  new_id = new_id.replace(/^\.|\.$/g, "");
  // 5. 빈 문자열이면 'a'
  if (new_id.length == 0) {
    new_id = "a";
  }
  // 6. 16자 이상이면 15개까지, 마지막 마침표 제거
  if (new_id.length > 15) {
    new_id = new_id.slice(0, 15);
    new_id = new_id.replace(/\.$/g, "");
  }
  // 7. 길이가 2자 이하면 마지막 문자 3까지 반복
  if (new_id.length < 3) {
    i = 3 - new_id.length;
    new_id = new_id + new_id[new_id.length - 1].repeat(i);
  }

  console.log(new_id);
}

solution("...!@BaT#*..y.abcdefghijklm");
solution("z-+.^.");
solution("=.=");
solution("123_.def");
solution("abcdefghijklmn.p");
