
# patch_index_unit1.py
# Replaces Unit 1 card in index.html with full 7-module version

with open('index.html', 'r', encoding='utf-8', errors='replace') as f:
    content = f.read()

# The block to find and replace
OLD_BLOCK = '''            <!-- UNIT 1 - Tous les modules -->
            <div class="unit-card unit-card--teal reveal" id="unit-1">
                <div class="unit-card-top">
                    <div class="unit-icon">🔬</div>
                    <div>
                        <div class="unit-number">الوحدة الأولى</div>
                        <div class="unit-title">جميع مقاييس الوحدة</div>
                    </div>
                </div>
                <p class="unit-description">
                    تشمل هذه الوحدة جميع ملخصات المقاييس: السيميولوجيا بأنواعها، الفيزيولوجيا المرضية، البيوكيمياء، والأشعة.
                </p>
                <div class="unit-modules-count">
                    📄 تحتوي على ملخصات شاملة ومكثفة
                </div>
                <div class="unit-btn-group">
                    <a href="Unité 1 - Sémiologie Générale.html" class="unit-btn unit-btn--primary">
                        <span>Sémiologie Générale</span>
                        <span class="btn-arrow">←</span>
                    </a>
                    <a href="Unité 1 - Sémiologie Pneumologique.html" class="unit-btn unit-btn--primary">
                        <span>Sémiologie Pneumologique</span>
                        <span class="btn-arrow">←</span>
                    </a>
                    <a href="Unité 1 - Sémiologie Cardiologique.html" class="unit-btn unit-btn--primary">
                        <span>Sémiologie Cardiologique</span>
                        <span class="btn-arrow">←</span>
                    </a>
                    <a href="Unité 1 - Physiopathologie.html" class="unit-btn unit-btn--secondary">
                        <span>Physiopathologie</span>
                        <span class="btn-arrow">←</span>
                    </a>
                    <a href="Unité 1 - Biochimie.html" class="unit-btn unit-btn--secondary">
                        <span>Biochimie</span>
                        <span class="btn-arrow">←</span>
                    </a>
                    <a href="Unité 1 - Radiologie.html" class="unit-btn unit-btn--secondary">
                        <span>Radiologie U1</span>
                        <span class="btn-arrow">←</span>
                    </a>
                </div>
            </div>'''

NEW_BLOCK = '''            <!-- UNIT 1 - Tous les modules -->
            <div class="unit-card unit-card--teal reveal" id="unit-1">
                <div class="unit-card-top">
                    <div class="unit-icon">🔬</div>
                    <div>
                        <div class="unit-number">الوحدة الأولى</div>
                        <div class="unit-title">جميع مقاييس الوحدة — 7 ملخصات</div>
                    </div>
                </div>
                <p class="unit-description">
                    السيميولوجيا العامة، القلبية والرئوية، الفيزيولوجيا المرضية، البيوكيمياء، الأشعة، وعلم النفس الطبي — 7 مقاييس كاملة.
                </p>
                <div class="unit-modules-count">
                    📚 7 مقاييس — ملخصات شاملة بالعربية والفرنسية
                </div>
                <div class="unit-btn-group">
                    <a href="Unité 1 - Sémiologie Générale.html" class="unit-btn unit-btn--primary">
                        <span>🩺 Sémiologie Générale</span>
                        <span class="btn-arrow">←</span>
                    </a>
                    <a href="Unité 1 - Sémiologie Pneumologique.html" class="unit-btn unit-btn--primary">
                        <span>🫁 Sémiologie Pneumologique</span>
                        <span class="btn-arrow">←</span>
                    </a>
                    <a href="Unité 1 - Sémiologie Cardiologique.html" class="unit-btn unit-btn--primary">
                        <span>🫀 Sémiologie Cardiologique</span>
                        <span class="btn-arrow">←</span>
                    </a>
                    <a href="Unité 1 - Physiopathologie.html" class="unit-btn unit-btn--secondary">
                        <span>⚗️ Physiopathologie</span>
                        <span class="btn-arrow">←</span>
                    </a>
                    <a href="Unité 1 - Biochimie.html" class="unit-btn unit-btn--secondary">
                        <span>🧪 Biochimie</span>
                        <span class="btn-arrow">←</span>
                    </a>
                    <a href="Unité 1 - Radiologie.html" class="unit-btn unit-btn--secondary">
                        <span>☢️ Radiologie U1</span>
                        <span class="btn-arrow">←</span>
                    </a>
                    <a href="Psychologie Médicale - Cours Complet.html" class="unit-btn unit-btn--secondary">
                        <span>🧠 Psychologie Médicale</span>
                        <span class="btn-arrow">←</span>
                    </a>
                </div>
            </div>'''

if OLD_BLOCK in content:
    content = content.replace(OLD_BLOCK, NEW_BLOCK, 1)
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print("SUCCESS: Unit 1 card updated with 7 modules.")
else:
    # Try to find what's there
    idx = content.find('unit-card--teal')
    if idx >= 0:
        print("BLOCK NOT MATCHED. Found teal card at char:", idx)
        print("Snippet:", content[idx:idx+300])
    else:
        print("ERROR: Could not find Unit 1 card at all!")
