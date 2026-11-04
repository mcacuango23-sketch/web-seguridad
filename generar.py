from pathlib import Path
from html import escape
ROOT=Path(__file__).parent
products=[
('Cámara IP Bullet 4 MP','Videovigilancia','bullet','Imagen detallada para vigilar accesos, patios y perímetros.',['4 MP · lente 2,8 mm','Infrarrojo hasta 30 m','PoE · protección IP67']),
('Cámara Domo IP 4 MP','Videovigilancia','dome','Una vista discreta para oficinas, locales y espacios interiores.',['4 MP · lente 2,8 mm','Compresión H.265','PoE · carcasa IK10']),
('Cámara Wi-Fi Interior','Videovigilancia','wifi','Revisa tu hogar desde el teléfono y conversa a través de la cámara.',['1080p · Wi-Fi 2,4 GHz','Giro horizontal de 355°','Audio bidireccional']),
('Grabador NVR 8 canales','Videovigilancia','nvr','Centraliza las cámaras IP y consulta tus grabaciones en un solo lugar.',['8 canales IP · H.265','Salida HDMI hasta 4K','1 bahía SATA · disco no incluido']),
('Videoportero IP con monitor','Acceso inteligente','intercom','Ve quién llama y conversa antes de abrir la puerta.',['Monitor táctil de 7 pulgadas','Cámara exterior de 2 MP','Audio bidireccional · relé']),
('Cerradura inteligente','Acceso inteligente','lock','Acceso práctico para tu puerta con distintos métodos de apertura.',['Huella · PIN · tarjeta','Alimentación con pilas AA','Llave mecánica de respaldo']),
('Terminal de huella y tarjeta','Acceso inteligente','reader','Organiza el acceso de tu equipo a oficinas y áreas restringidas.',['Hasta 1.000 huellas','RFID de 13,56 MHz','Ethernet · salida de relé']),
('Kit de alarma inalámbrica','Alarmas','alarm','Detecta aperturas y movimiento en los espacios de tu hogar.',['Panel Wi-Fi 2,4 GHz','1 PIR + 1 contacto magnético','1 sirena + 2 controles']),
('Detector de movimiento PIR','Alarmas','pir','Complementa tu alarma con detección de movimiento en interiores.',['Cobertura de hasta 12 m','Ángulo de detección de 90°','Relé · alimentación 12 V CC']),
('Switch PoE de 8 puertos','Redes y energía','switch','Conecta y alimenta tus cámaras por el mismo cable de red.',['8 PoE+ + 2 uplink Gigabit','Presupuesto PoE total: 120 W','IEEE 802.3af/at'])]
def svg(kind,label):
    s='fill="#edf1e9" stroke="#365c49" stroke-width="2" stroke-linejoin="round"'
    lens='<circle cx="150" cy="103" r="25" fill="#17382f"/><circle cx="150" cy="103" r="15" fill="#486c5d"/><circle cx="150" cy="103" r="8" fill="#0a211a"/><circle cx="145" cy="97" r="4" fill="#a7ddc0"/>'
    shapes={
    'bullet':'<path d="M187 117l31 28v22h29v10h-41v-27l-30-24" '+s+'/><path d="M80 58h114l24 23-25 57H80L62 112V78z" '+s+'/><path d="M76 56h127l18 22H63z" fill="#fafcf7" stroke="#365c49" stroke-width="2"/><ellipse cx="90" cy="105" rx="24" ry="32" fill="#17382f"/><ellipse cx="90" cy="105" rx="14" ry="20" fill="#486c5d"/><ellipse cx="90" cy="105" rx="8" ry="12" fill="#0b211a"/><circle cx="86" cy="98" r="4" fill="#a7ddc0"/>',
    'dome':'<ellipse cx="150" cy="75" rx="74" ry="22" '+s+'/><path d="M78 78c0 87 144 87 144 0" fill="#587866" stroke="#365c49" stroke-width="2"/>'+lens+'<ellipse cx="150" cy="69" rx="64" ry="12" fill="#f8fbf3"/>',
    'wifi':'<path d="M122 134l-12 40h82l-12-40" '+s+'/><rect x="103" y="43" width="94" height="103" rx="40" '+s+'/>'+lens+'<path d="M212 60q14 12 0 25m9-34q25 21 0 43" fill="none" stroke="#739c87" stroke-width="3"/>',
    'nvr':'<path d="M59 83l32-29h149l-24 29z" fill="#67816e" stroke="#365c49" stroke-width="2"/><rect x="59" y="83" width="157" height="62" rx="5" fill="#234b37"/><path d="M76 122h92" stroke="#758d77" stroke-width="3"/><circle cx="195" cy="116" r="3" fill="#d2ed94"/>',
    'intercom':'<rect x="42" y="67" width="144" height="97" rx="7" '+s+'/><rect x="54" y="79" width="120" height="65" fill="#365c49"/><path d="M62 137l36-39 23 22 20-12 24 29" fill="#8cac8b"/><circle cx="114" cy="154" r="3" fill="#365c49"/><rect x="202" y="36" width="45" height="134" rx="8" fill="#365c49"/><circle cx="224" cy="64" r="13" fill="#0b211a"/><circle cx="224" cy="142" r="9" fill="#c2e496"/>',
    'lock':'<rect x="124" y="27" width="53" height="155" rx="13" fill="#365c49"/><rect x="132" y="38" width="37" height="55" rx="4" fill="#17382f"/><g fill="#c9ddbd"><circle cx="142" cy="54" r="2"/><circle cx="153" cy="54" r="2"/><circle cx="164" cy="54" r="2"/><circle cx="142" cy="67" r="2"/><circle cx="153" cy="67" r="2"/><circle cx="164" cy="67" r="2"/></g><rect x="146" y="109" width="91" height="15" rx="7" fill="#b7c2b3" stroke="#365c49" stroke-width="2"/><circle cx="150" cy="154" r="8" fill="#17382f"/>',
    'reader':'<rect x="100" y="28" width="103" height="155" rx="12" fill="#365c49"/><rect x="112" y="42" width="79" height="49" rx="4" fill="#a4bc9a"/><path d="M128 77v-17h45v17" fill="none" stroke="#365c49" stroke-width="2"/><rect x="133" y="103" width="37" height="38" rx="6" fill="#17382f"/><path d="M143 132v-17q9-11 17 0v17m-12 0v-14q4-5 8 0v14" fill="none" stroke="#acd19f" stroke-width="2"/><path d="M119 159h65m-65 10h65" stroke="#a4bc9a" stroke-dasharray="5 6" stroke-width="3"/>',
    'alarm':'<rect x="65" y="47" width="116" height="120" rx="20" '+s+'/><path d="M121 74l22 9v22q-5 15-22 22-17-7-22-22V83z" fill="#8cab7a"/><path d="M110 98l8 8 16-19" fill="none" stroke="#fff" stroke-width="3"/><rect x="201" y="76" width="27" height="82" rx="8" '+s+'/><rect x="236" y="76" width="12" height="82" rx="5" '+s+'/>',
    'pir':'<rect x="110" y="33" width="81" height="149" rx="27" '+s+'/><path d="M124 102h54v49q-27 17-54 0z" fill="#bfd0b9" stroke="#779782"/><path d="M125 113h52m-52 12h52m-52 12h52" stroke="#eff4ee" stroke-width="2"/><circle cx="151" cy="70" r="4" fill="#73926e"/>',
    'switch':'<path d="M50 90l33-29h163l-22 29z" fill="#849a7e" stroke="#365c49" stroke-width="2"/><rect x="50" y="90" width="174" height="57" rx="5" fill="#365c49"/>'+''.join(f'<rect x="{61+i*15}" y="111" width="11" height="14" rx="1" fill="#17382f"/><circle cx="{64+i*15}" cy="104" r="1.8" fill="#d2ed94"/>' for i in range(10))}
    return '<svg viewBox="0 0 300 210" role="img" aria-label="'+escape(label)+'" xmlns="http://www.w3.org/2000/svg"><ellipse cx="151" cy="187" rx="93" ry="8" fill="#17382f" opacity=".08"/>'+shapes[kind]+'</svg>'
cards=''
for i,(name,cat,kind,desc,specs) in enumerate(products,1):
    cards+=f'<article class="card" data-category="{cat}" data-search="{escape(name+" "+cat+" "+desc+" "+" ".join(specs))}"><div class="product-art"><span class="ref">NX-{i:03}</span>{svg(kind,name)}</div><div class="card-body"><p class="eyebrow">{cat}</p><h3>{name}</h3><p class="description">{desc}</p><ul>'+''.join('<li>'+escape(s)+'</li>' for s in specs)+f'</ul><button class="quote" data-product="{name}" type="button">Cotizar producto <span aria-hidden="true">↗</span></button></div></article>'
template=(ROOT/'plantilla.html').read_text(encoding='utf-8')
html=template.replace('<!--HERO-->',svg('bullet','Ilustración de cámara IP Bullet')).replace('<!--PRODUCTS-->',cards).replace('<!--OPTIONS-->',''.join('<option>'+escape(p[0])+'</option>' for p in products))
(ROOT/'dist'/'index.html').write_text(html,encoding='utf-8')
table=['| Producto | Categoría | Especificaciones de ejemplo |','|---|---|---|']+['| '+p[0]+' | '+p[1]+' | '+'; '.join(p[4])+' |' for p in products]
(ROOT/'PRODUCTOS.md').write_text('# Productos de ejemplo\n\nMarca ficticia: NEXO Seguridad. Equipos genéricos sin referencia comercial.\n\n'+'\n'.join(table)+'\n',encoding='utf-8')
print('Generado index.html con 10 productos e ilustraciones SVG integradas.')
