content = open('index.html', 'r', encoding='utf-8').read()
animations = '''<style>
@keyframes float {
  0%, 100% { transform: translateY(0px); }
  50% { transform: translateY(-12px); }
}
@keyframes glow-gold {
  0%, 100% { text-shadow: 0 0 10px rgba(255,215,0,0.3); }
  50% { text-shadow: 0 0 40px rgba(255,215,0,0.9), 0 0 80px rgba(255,215,0,0.4); }
}
@keyframes shimmer {
  0% { background-position: -200% center; }
  100% { background-position: 200% center; }
}
@keyframes pulse-border-gold {
  0%, 100% { box-shadow: 0 0 10px rgba(255,215,0,0.2), inset 0 0 10px rgba(255,215,0,0.05); }
  50% { box-shadow: 0 0 30px rgba(255,215,0,0.5), inset 0 0 20px rgba(255,215,0,0.1); }
}
@keyframes pulse-border-green {
  0%, 100% { box-shadow: 0 0 10px rgba(0,255,136,0.2), inset 0 0 10px rgba(0,255,136,0.05); }
  50% { box-shadow: 0 0 30px rgba(0,255,136,0.5), inset 0 0 20px rgba(0,255,136,0.1); }
}
@keyframes pulse-border-red {
  0%, 100% { box-shadow: 0 0 10px rgba(231,0,19,0.2), inset 0 0 10px rgba(231,0,19,0.05); }
  50% { box-shadow: 0 0 30px rgba(231,0,19,0.5), inset 0 0 20px rgba(231,0,19,0.1); }
}
@keyframes spin3d {
  0% { transform: rotateY(0deg) scale(1); }
  50% { transform: rotateY(180deg) scale(1.1); }
  100% { transform: rotateY(360deg) scale(1); }
}
@keyframes fadeInUp {
  from { opacity: 0; transform: translateY(40px); }
  to   { opacity: 1; transform: translateY(0); }
}
@keyframes particles {
  0%   { transform: translateY(0) rotate(0deg); opacity: 1; }
  100% { transform: translateY(-100px) rotate(720deg); opacity: 0; }
}
/* Title animation */
#page-home h1 {
  animation: float 3s ease-in-out infinite, glow-gold 2.5s ease-in-out infinite !important;
  background: linear-gradient(90deg, #FFD700, #fff, #FFD700, #FFA500, #FFD700);
  background-size: 200% auto;
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
  animation: float 3s ease-in-out infinite, shimmer 3s linear infinite !important;
}
/* Cards entrance animation */
.home-btn {
  animation: fadeInUp 0.6s ease both;
}
.home-btn:nth-child(1) { animation-delay: 0.1s; }
.home-btn:nth-child(2) { animation-delay: 0.25s; }
.home-btn:nth-child(3) { animation-delay: 0.4s; }
/* Gold card pulse */
button[style*="FFD700"][style*="border:2px solid"] {
  animation: pulse-border-gold 2.5s ease-in-out infinite;
}
/* Green card pulse */
button[style*="00ff88"][style*="border:2px solid"] {
  animation: pulse-border-green 2.5s ease-in-out infinite;
}
/* Red card pulse */
button[style*="E70013"][style*="border:2px solid"] {
  animation: pulse-border-red 2.5s ease-in-out infinite;
}
/* Image 3D hover */
.home-btn:hover .btn-icon {
  animation: spin3d 0.7s ease forwards !important;
  filter: drop-shadow(0 20px 40px rgba(255,215,0,0.8)) !important;
}
.home-btn-green:hover .btn-icon {
  filter: drop-shadow(0 20px 40px rgba(0,255,136,0.8)) !important;
}
/* Subtitle shimmer */
#page-home p {
  background: linear-gradient(90deg, #555, #aaa, #555);
  background-size: 200% auto;
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
  animation: shimmer 4s linear infinite;
}
/* Developer card subtle glow */
#page-home > div[style*="bottom:20px"] {
  animation: fadeInUp 1s ease 0.5s both;
  transition: box-shadow 0.3s;
}
#page-home > div[style*="bottom:20px"]:hover {
  box-shadow: 0 0 20px rgba(255,215,0,0.3) !important;
}
</style>'''
content = content.replace('</head>', animations + '</head>', 1)
open('index.html', 'w', encoding='utf-8').write(content)
print('done')
