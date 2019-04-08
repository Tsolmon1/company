from datetime import datetime
from flask import render_template, flash, redirect, url_for, request, g, \
    jsonify, current_app
from flask_login import current_user, login_required
from flask_babel import _, get_locale
#from guess_language import guess_language
from app import db
from app.main.forms import CompanyForm
from app.models import Company_list

from app.main import bp




@bp.route("/company", methods=['GET'])
def company_namelist():
    """
    List all company
    """

    #loan_requests = Loan_request.query.all()
    page = request.args.get('page', 1, type=int)
    companys = Company_list.query.order_by(Company_list.id.asc()).paginate(
        page, current_app.config['POSTS_PER_PAGE'], False)

    next_url = url_for('main.company_namelist', page=companys.next_num) \
        if companys.has_next else None
    prev_url = url_for('main.company_namelist', page=companys.prev_num) \
        if companys.has_prev else None

    return render_template('company/company_namelists.html', companys=companys.items, title="companys", next_url=next_url, prev_url=prev_url)

@bp.route('/company/add', methods=['GET', 'POST'])
def add_company():
    form = CompanyForm()
    if form.validate_on_submit():
        company = Company_list(names_one=form.names_one.data,
                            names_two=form.names_two.data,
                            names_three=form.names_three.data,
                            branches=form.branches.data)

        # add employee to the database
        db.session.add(company)
        db.session.commit()
        flash('You have successfully registered!')

        # redirect to the login page
        return redirect(url_for('main.company_namelist'))

    # load registration template
    return render_template('company/company_add.html', form=form, title='LoanTypeAdd')
    
@bp.route('/companys/edit/<int:id>', methods=['GET', 'POST'])


def edit_company(id):
    """
    Edit a user
    """

    add_company = False

    companys = Company_list.query.get_or_404(id)
    form = CompanyForm(obj=companys)
    if form.validate_on_submit():

        companys.names_one = form.names_one.data
        companys.names_two = form.names_two.data
        companys.names_three = form.names_three.data
        companys.branches = form.branches.data

        db.session.add(companys)
        db.session.commit()
        flash('You have successfully edited the companys.')

        # redirect to the roles page
        return redirect(url_for('main.company_namelist'))

    form.names_one.data = companys.names_one
    form.names_two.data = companys.names_two
    form.names_three.data = companys.names_three
    form.branches.data = companys.branches

    return render_template('company/company_edit.html', add_company=add_company,
                           form=form, title="Edit company")

@bp.route('/company/delete/<int:id>', methods=['GET', 'POST'])

def delete_company(id):
    """
    Delete a employee from the database
    """

    companyss = Company_list.query.get_or_404(id)
    db.session.delete(companyss)
    db.session.commit()
    flash('You have successfully deleted the company.')

    # redirect to the roles page
    return redirect(url_for('main.company_namelist'))