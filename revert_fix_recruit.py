import re

file_path = "recruit.html"

with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# 1. Mobile Menu Logo (Revert back to original)
current_menu = """   <div class="sticky top-0 bg-white/95 backdrop-blur-sm z-10 px-6 h-20 flex justify-end items-center border-b border-gray-100">
   <button id="mobile-close-btn" class="text-gray-500 hover:text-main-red transition-colors w-10 h-10 flex items-center justify-center  hover:bg-gray-100 focus:outline-none">"""
original_menu = """   <div class="sticky top-0 bg-white/95 backdrop-blur-sm z-10 px-6 h-20 flex justify-between items-center border-b border-gray-100">
   <a href="#" class="flex items-center gap-3">
    <img src="img/img-main/logo.png" alt="T.RAD 株式会社ティラド" class="h-8 w-auto object-contain">
    <span class="font-bold text-xs tracking-[0.2em] text-gray-400 border-l-2 pl-3 border-gray-300 mt-0.5">RECRUIT</span>
   </a>
   <button id="mobile-close-btn" class="text-gray-500 hover:text-main-red transition-colors w-10 h-10 flex items-center justify-center  hover:bg-gray-100 focus:outline-none">"""
content = content.replace(current_menu, original_menu)

# 2. FV layout (Revert back to original)
current_fv = """    <section class="relative w-full lg:aspect-video block lg:flex lg:items-center pt-20 lg:pb-12 overflow-hidden bg-white lg:bg-black">
      <!-- YouTube Video Background -->
      <div class="relative lg:absolute lg:inset-x-0 lg:bottom-0 lg:top-20 xl:top-0 z-0 overflow-hidden pointer-events-none w-full aspect-video lg:aspect-auto">
        <video 
          class="absolute top-1/2 left-1/2 w-full h-full -translate-x-1/2 -translate-y-1/2 object-cover"
          src="img/img-recruit/fv.mp4" 
          autoplay loop muted playsinline>
        </video>
      </div>"""
original_fv = """    <section class="relative w-full md:h-[100vh] md:min-h-[600px] block md:flex md:items-center pt-20 md:pb-12 overflow-hidden bg-white md:bg-black">
      <!-- YouTube Video Background -->
      <div class="relative md:absolute md:inset-0 z-0 overflow-hidden pointer-events-none w-full aspect-video md:aspect-auto">
        <video 
          class="absolute top-1/2 left-1/2 w-full h-full md:w-[150%] md:h-[150%] lg:w-[110%] lg:h-[110%] md:min-w-[177.77vh] md:min-h-[100vh] -translate-x-1/2 -translate-y-1/2 object-cover"
          src="img/img-recruit/fv.mp4" 
          autoplay loop muted playsinline>
        </video>
      </div>"""
content = content.replace(current_fv, original_fv)

# 3. Catchphrase size (Revert back to original)
current_h1 = """        <h1 class="font-black text-5xl sm:text-7xl md:text-[80px] leading-[1.1] tracking-tighter md:drop-shadow-2xl mb-4">"""
original_h1 = """        <h1 class="font-black text-5xl sm:text-7xl md:text-8xl lg:text-[7.5rem] leading-[1.1] tracking-tighter md:drop-shadow-2xl mb-4">"""
content = content.replace(current_h1, original_h1)

with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)

print("Reverted successfully")
