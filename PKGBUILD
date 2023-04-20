pkgname=jupiter-firewall
pkgver=0.1
pkgrel=1
arch=('any')
license=('MIT')
pkgdesc="Jupiter Firewall Configuration"
url='https://gitlab.steamos.cloud/holo'
depends=('nftables' 'firewalld')
sha256sums=('2b8e5cd114d6944624507834391edcffde9dabb4fb8f2e611c0bf39c4b03e833'
            'feef41d5bd5ff06a24d1283a44fa0aab6f5965518bd883a764407ea17ed06bd6')

source=("org.fedoraproject.FirewallD1.rules" "firewalld_zones_public.xml")

package() {
	# Preserve polkit permissions
	install -dm750 -o root -g 102 "$pkgdir"/usr/share/polkit-1/rules.d
	install -Dm644 "$srcdir"/org.fedoraproject.FirewallD1.rules \
		-t "$pkgdir"/usr/share/polkit-1/rules.d/

	# Default rules for the "public" zone, installed to /etc so that this
	# package doesn't conflict with the firewalld package. Users can still
	# append to or override these.
	install -Dm644 "$srcdir"/firewalld_zones_public.xml \
		"$pkgdir"/etc/firewalld/zones/public.xml
}
