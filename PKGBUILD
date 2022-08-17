# Maintainer: John Schoenick <johns@valvesoftware.com>

pkgname=foxnet
pkgver=1.3
pkgrel=1
pkgdesc="Foxnet and various paraphernalia"
arch=(any)
depends=(python3 python-psutil python-aiohttp nvme-cli foxnetstatsd)
source=(foxnet.service
        foxnet-init
        foxnet-updater-fixup
        foxnet-updater-fixup.service)
sha256sums=('0200d280e1c7acf67f7856014dd2fb2b3e2425f2d486752a583c24defa275680'
            '518db678d2f36bb13c869b6a02cde1fe4eec306045c331a42a903f37ca678bef'
            '4e07aef852bd826fdb7d299c57f75ed3c50dd501a8bf485ba4e910080725228a'
            '1cf0f6e640fbe9eb63c46ff168a52f87f701c38afa102b63046ba28591ee458e')

package() {
  mkdir -p -m755 "$pkgdir"/etc/systemd/system/multi-user.target.wants

  # Foxnet updater fixup thing
  install -D -m755 "$srcdir"/foxnet-updater-fixup "$pkgdir"/usr/bin/foxnet-updater-fixup
  install -D -m755 -t "$pkgdir"/etc/systemd/system "$srcdir"/foxnet-updater-fixup.service
  ln -sv ../foxnet-updater-fixup.service "$pkgdir"/etc/systemd/system/multi-user.target.wants/

  # foxnet
  install -D -m755 -t "$pkgdir"/etc/systemd/system "$srcdir"/foxnet.service
  ln -sv ../foxnet.service "$pkgdir"/etc/systemd/system/multi-user.target.wants/

  install -D -m755 -t "$pkgdir"/usr/bin "$srcdir"/foxnet-init
}
