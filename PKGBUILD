# Maintainer: Holo Team

pkgname=steamos-alias
pkgver=2.0
pkgrel=1
pkgdesc="Provides aliasing to legacy steamos naming for holo utilities."
arch=(any)
license=('MIT')
source=(
        manage-steamos-aliases
        manage-steamos-aliases.hook
)
sha256sums=('fea6db4d4168ea3bf535fd74d0942e3b2a5567535283ad201fc8c3805d92df86'
            '4d96b0542b996a74b7dce01ad8b17f78212aeca678610a307b6e7790bbe35ae9')

package() {
  # pacman hook to create and destroy aliases as packages installed and removed
  install -D -m755 "$srcdir"/manage-steamos-aliases "$pkgdir"/usr/share/libalpm/scripts/manage-steamos-aliases
  install -D -m644 "$srcdir"/manage-steamos-aliases.hook "$pkgdir"/usr/share/libalpm/hooks/manage-steamos-aliases.hook
}
