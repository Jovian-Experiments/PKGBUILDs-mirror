# Maintainer Ethan Geller (ethang@valvesoftware.com)

pkgname=neptune-ctl
_srctag=20230928.1
pkgver=${_srctag#galileo-}
pkgrel=3
arch=('any')
url=""
pkgdesc="Neptune CTL"
license=('Proprietary')
depends=('python-pyserial' 'python-click' 'python-pylink-square' 'python-hexdump' 'python>=3.11' 'python<3.12')
source=(neptunectl.py
        neptune-ctl
)
sha512sums=('2faaff2f08438f5ea1af815d2a5fa22db031ff865b29f08d592e70ff15c3aa3a73f92bfadcec97396e2030a66bde50c14023ea628c8c376f746de28e86c80bb2'
            '5b19cd8026b63a363ddd5118c6c80b2272cd463a3688aefce14f678238652729c11be5db0bb868b94231b7461624f76818025abb1168d3b39be27a60c880b61b')

package() {
  install -D -m755 -t "$pkgdir"/usr/lib/neptunectl "$srcdir"/neptunectl.py
  install -D -m755 -t "$pkgdir"/usr/bin "$srcdir"/neptune-ctl
}
