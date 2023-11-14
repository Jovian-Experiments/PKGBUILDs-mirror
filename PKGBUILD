# Maintainer: John Schoenick <johns@valvesoftware.com>

pkgname=foxnet
pkgver=1.5
pkgrel=1
pkgdesc="Foxnet and various paraphernalia"
arch=(any)
depends=(python3 python-psutil python-aiohttp nvme-cli foxnetstatsd)
source=(foxnet.service
        foxnet-init)
sha256sums=('0200d280e1c7acf67f7856014dd2fb2b3e2425f2d486752a583c24defa275680'
            '67b34113b12ef215b0a5423e1792d5463a13debda88855f795646446bd82cfdd')

package() {
  # foxnet
  mkdir -p -m755 "$pkgdir"/etc/systemd/system/multi-user.target.wants
  install -D -m755 -t "$pkgdir"/etc/systemd/system "$srcdir"/foxnet.service
  ln -sv ../foxnet.service "$pkgdir"/etc/systemd/system/multi-user.target.wants/

  install -D -m755 -t "$pkgdir"/usr/bin "$srcdir"/foxnet-init
}
