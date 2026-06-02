import re

file_path = "recruit.html"

with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# 1. Mobile Menu Logo
old_menu = """   <div class="sticky top-0 bg-white/95 backdrop-blur-sm z-10 px-6 h-20 flex justify-between items-center border-b border-gray-100">
   <a href="#" class="flex items-center gap-3">
    <img src="img/img-main/logo.png" alt="T.RAD 株式会社ティラド" class="h-8 w-auto object-contain">
    <span class="font-bold text-xs tracking-[0.2em] text-gray-400 border-l-2 pl-3 border-gray-300 mt-0.5">RECRUIT</span>
   </a>
   <button id="mobile-close-btn" class="text-gray-500 hover:text-main-red transition-colors w-10 h-10 flex items-center justify-center  hover:bg-gray-100 focus:outline-none">"""
new_menu = """   <div class="sticky top-0 bg-white/95 backdrop-blur-sm z-10 px-6 h-20 flex justify-end items-center border-b border-gray-100">
   <button id="mobile-close-btn" class="text-gray-500 hover:text-main-red transition-colors w-10 h-10 flex items-center justify-center  hover:bg-gray-100 focus:outline-none">"""
content = content.replace(old_menu, new_menu)

# 2. FV layout
old_fv = """    <section class="relative w-full md:h-[100vh] md:min-h-[600px] block md:flex md:items-center pt-20 md:pb-12 overflow-hidden bg-white md:bg-black">
      <!-- YouTube Video Background -->
      <div class="relative md:absolute md:inset-0 z-0 overflow-hidden pointer-events-none w-full aspect-video md:aspect-auto">
        <video 
          class="absolute top-1/2 left-1/2 w-full h-full md:w-[150%] md:h-[150%] lg:w-[110%] lg:h-[110%] md:min-w-[177.77vh] md:min-h-[100vh] -translate-x-1/2 -translate-y-1/2 object-cover"
          src="img/img-recruit/fv.mp4" 
          autoplay loop muted playsinline>
        </video>
      </div>"""
new_fv = """    <section class="relative w-full lg:aspect-video block lg:flex lg:items-center pt-20 lg:pb-12 overflow-hidden bg-white lg:bg-black">
      <!-- YouTube Video Background -->
      <div class="relative lg:absolute lg:inset-x-0 lg:bottom-0 lg:top-20 xl:top-0 z-0 overflow-hidden pointer-events-none w-full aspect-video lg:aspect-auto">
        <video 
          class="absolute top-1/2 left-1/2 w-full h-full -translate-x-1/2 -translate-y-1/2 object-cover"
          src="img/img-recruit/fv.mp4" 
          autoplay loop muted playsinline>
        </video>
      </div>"""
content = content.replace(old_fv, new_fv)

# 3. Catchphrase size
old_h1 = """        <h1 class="font-black text-5xl sm:text-7xl md:text-8xl lg:text-[7.5rem] leading-[1.1] tracking-tighter md:drop-shadow-2xl mb-4">"""
new_h1 = """        <h1 class="font-black text-5xl sm:text-7xl md:text-[80px] leading-[1.1] tracking-tighter md:drop-shadow-2xl mb-4">"""
content = content.replace(old_h1, new_h1)

# 4. Categories Layout
# Extract the whole categories block
start_tag = "   <!-- 募集区分 (HIRING CATEGORY) -->\n"
end_tag = "   </section>\n"
start_idx = content.find(start_tag)
# find the next </section> after start_idx
end_idx = content.find(end_tag, start_idx) + len(end_tag)

new_categories = """   <!-- 募集区分 (HIRING CATEGORY) -->
   <section id="categories" class="py-20 md:py-32 relative scroll-mt-20 overflow-hidden bg-white">
      <div class="max-w-7xl mx-auto px-4 md:px-8 relative z-10">
        
        <!-- 上段：セクションタイトル -->
        <div class="mb-12 md:mb-16 fade-in-up text-center lg:text-left">
          <span class="text-xs font-bold tracking-[0.2em] text-gray-400 uppercase mb-4 block">HIRING CATEGORY</span>
          <h2 class="text-3xl md:text-5xl lg:text-6xl font-black tracking-wider leading-tight">
            <span class="scroll-text-gradient inline-block text-nowrap">募集区分</span>
          </h2>
        </div>

        <!-- 下段 -->
        <div class="flex flex-col lg:flex-row gap-8 lg:gap-16 lg:items-stretch">
          <!-- 下段（左）：画像 -->
          <div class="w-full lg:w-1/2 fade-in-up" style="transition-delay: 0.2s;">
            <div class="w-full h-full min-h-[300px] md:min-h-[400px] lg:min-h-[500px] overflow-hidden rounded-xl shadow-lg relative">
              <img src="img/img-recruit/hiring-category.jpg" alt="募集区分" class="absolute inset-0 w-full h-full object-cover group-hover:scale-105 transition-transform duration-700">
            </div>
          </div>
          
          <!-- 下段（右）：項目 -->
          <div class="w-full lg:w-1/2 flex flex-col justify-center fade-in-up" style="transition-delay: 0.4s;">
            <div class="flex flex-col border-t border-gray-200 bg-white shadow-sm rounded-lg overflow-hidden">
              
              <!-- 1. 新卒 -->
              <a id="new-grad" href="#" class="group py-5 md:py-6 lg:py-8 border-b border-gray-200 flex items-center justify-between transition-all duration-300 hover:bg-gray-50 hover:pl-4">
                <div class="flex items-center gap-4 md:gap-6 px-4 md:px-6">
                  <div class="w-10 h-10 md:w-12 md:h-12 flex items-center justify-center rounded-full bg-gray-50 group-hover:bg-red-50 transition-colors border border-gray-100 group-hover:border-red-100 shrink-0">
                    <i class="fa-solid fa-graduation-cap text-lg md:text-xl text-gray-400 group-hover:text-main-red transition-colors"></i>
                  </div>
                  <h3 class="text-base md:text-lg lg:text-xl font-bold text-gray-800 tracking-widest leading-normal">新卒採用</h3>
                </div>
                <div class="mr-4 md:mr-6 w-8 h-8 md:w-10 md:h-10 rounded-full border border-gray-200 flex items-center justify-center text-gray-400 group-hover:border-main-red group-hover:bg-main-red group-hover:text-white transition-all duration-300 shrink-0">
                  <i class="fa-solid fa-arrow-right text-sm"></i>
                </div>
              </a>

              <!-- 2. キャリア・カムバック -->
              <a id="career-grad" href="#" class="group py-5 md:py-6 lg:py-8 border-b border-gray-200 flex items-center justify-between transition-all duration-300 hover:bg-gray-50 hover:pl-4">
                <div class="flex items-center gap-4 md:gap-6 px-4 md:px-6">
                  <div class="w-10 h-10 md:w-12 md:h-12 flex items-center justify-center rounded-full bg-gray-50 group-hover:bg-red-50 transition-colors border border-gray-100 group-hover:border-red-100 shrink-0">
                    <i class="fa-solid fa-briefcase text-lg md:text-xl text-gray-400 group-hover:text-main-red transition-colors"></i>
                  </div>
                  <h3 class="text-base md:text-lg lg:text-xl font-bold text-gray-800 tracking-widest leading-tight md:whitespace-nowrap">キャリア・<br class="md:hidden">カムバック採用</h3>
                </div>
                <div class="mr-4 md:mr-6 w-8 h-8 md:w-10 md:h-10 rounded-full border border-gray-200 flex items-center justify-center text-gray-400 group-hover:border-main-red group-hover:bg-main-red group-hover:text-white transition-all duration-300 shrink-0">
                  <i class="fa-solid fa-arrow-right text-sm"></i>
                </div>
              </a>

              <!-- 3. 高卒 -->
              <a href="#" class="group py-5 md:py-6 lg:py-8 border-b border-gray-200 flex items-center justify-between transition-all duration-300 hover:bg-gray-50 hover:pl-4">
                <div class="flex items-center gap-4 md:gap-6 px-4 md:px-6">
                  <div class="w-10 h-10 md:w-12 md:h-12 flex items-center justify-center rounded-full bg-gray-50 group-hover:bg-red-50 transition-colors border border-gray-100 group-hover:border-red-100 shrink-0">
                    <i class="fa-solid fa-school text-lg md:text-xl text-gray-400 group-hover:text-main-red transition-colors"></i>
                  </div>
                  <h3 class="text-base md:text-lg lg:text-xl font-bold text-gray-800 tracking-widest leading-normal">高卒採用</h3>
                </div>
                <div class="mr-4 md:mr-6 w-8 h-8 md:w-10 md:h-10 rounded-full border border-gray-200 flex items-center justify-center text-gray-400 group-hover:border-main-red group-hover:bg-main-red group-hover:text-white transition-all duration-300 shrink-0">
                  <i class="fa-solid fa-arrow-right text-sm"></i>
                </div>
              </a>

              <!-- 4. 障がい者 -->
              <a href="#" class="group py-5 md:py-6 lg:py-8 border-b border-gray-200 flex items-center justify-between transition-all duration-300 hover:bg-gray-50 hover:pl-4">
                <div class="flex items-center gap-4 md:gap-6 px-4 md:px-6">
                  <div class="w-10 h-10 md:w-12 md:h-12 flex items-center justify-center rounded-full bg-gray-50 group-hover:bg-red-50 transition-colors border border-gray-100 group-hover:border-red-100 shrink-0">
                    <i class="fa-solid fa-hands-holding-circle text-lg md:text-xl text-gray-400 group-hover:text-main-red transition-colors"></i>
                  </div>
                  <h3 class="text-base md:text-lg lg:text-xl font-bold text-gray-800 tracking-widest leading-normal">障がい者採用</h3>
                </div>
                <div class="mr-4 md:mr-6 w-8 h-8 md:w-10 md:h-10 rounded-full border border-gray-200 flex items-center justify-center text-gray-400 group-hover:border-main-red group-hover:bg-main-red group-hover:text-white transition-all duration-300 shrink-0">
                  <i class="fa-solid fa-arrow-right text-sm"></i>
                </div>
              </a>

              <!-- 5. グループ会社 -->
              <a href="#" class="group py-5 md:py-6 lg:py-8 border-b border-transparent flex items-center justify-between transition-all duration-300 hover:bg-gray-50 hover:pl-4">
                <div class="flex items-center gap-4 md:gap-6 px-4 md:px-6">
                  <div class="w-10 h-10 md:w-12 md:h-12 flex items-center justify-center rounded-full bg-gray-50 group-hover:bg-red-50 transition-colors border border-gray-100 group-hover:border-red-100 shrink-0">
                    <i class="fa-solid fa-city text-lg md:text-xl text-gray-400 group-hover:text-main-red transition-colors"></i>
                  </div>
                  <h3 class="text-base md:text-lg lg:text-xl font-bold text-gray-800 tracking-widest leading-normal">グループ会社採用</h3>
                </div>
                <div class="mr-4 md:mr-6 w-8 h-8 md:w-10 md:h-10 rounded-full border border-gray-200 flex items-center justify-center text-gray-400 group-hover:border-main-red group-hover:bg-main-red group-hover:text-white transition-all duration-300 shrink-0">
                  <i class="fa-solid fa-arrow-right text-sm"></i>
                </div>
              </a>

            </div>
          </div>
        </div>
      </div>
    </section>\n"""
content = content[:start_idx] + new_categories + content[end_idx:]

with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)

print("Done")
