# Maintainer: Vlad Zahorodnii <vladzzag@gmail.com>
pkgname=drm_janitor
pkgver=0.0.3
pkgrel=1
pkgdesc="A helper that resets the DRM state to reasonable defaults"
arch=(x86_64)
url="https://github.com/zzag/drm_janitor"
license=('MIT')
depends=(libdrm)
makedepends=(meson)
source=("$pkgname-$pkgver.tar.gz"::"https://github.com/zzag/$pkgname/archive/$pkgver.tar.gz"
        drm_janitor.conf)
sha256sums=('8a735afcd1117a6dadd083cfa532b66f57d09e4996846fa7a25f563dcffb8656'
            'SKIP')

build() {
    arch-meson build "${pkgname}-${pkgver}"
    meson compile -C build
}

package() {
    meson install -C build --destdir="${pkgdir}"
    install -Dm644 "${pkgname}-${pkgver}/LICENSE" "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
    install -Dm644 drm_janitor.conf "${pkgdir}/usr/lib/systemd/system/sddm.service.d/drm_janitor.conf"
}
